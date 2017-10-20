var express = require('express');
var router = express.Router();
var auth = require("../core/auth");
var user = require("../core/user");
var chatHandler = require("../core/chat");

function get_token(request){
    return request.body.token; // change this later
}

router.post('/authenticate', function (req, res) {
	// authenticate the user, give him a token or reply with an error.
    // on success: {success: true, token: token}
    // on error: {success: false, error: err_msg}
    auth.auth(req.body, function(result){
        res.send(result);
    });
});

// get all users.
router.get('/users', function (req, res) {
    user.get_all(function(names){
        res.json({user_names: names});
    });
});

// register the user, expects a username, password and email, the password must be encrypted already.
// on success return a JSON object {success: true, error: ""}
 // on error return a JSON object {success: false, error: err_msg}
router.post('/register', function(req, res){

    user.create_user(req.body, function(result){
            return res.json(result);
        });
});

router.delete("/delete/:token", function(req, res)
{
	// delete the user.
});

var current_token = null;
// require authetication for all /auth/*
// authenticate the user, if the user is not authenticated, respond with forbidden.
router.all("/auth/*", function(req, res, next){
    current_token = get_token(req);
    console.log("authenticating with: " + current_token);
    if(auth.is_auth(current_token))
    {
        // token is valid, proceed
        next();
        return;
    }
    // if token is invaild return forbidden
    res.status(403);
    res.send("Forbidden");

});

// log out the user, destroy token.
router.post("/auth/logout", function(req, res){
    auth.remove(current_token);
    res.send("logged out");
});


router.post('/auth/test', function (req, res) {
  res.send('Birds home page');
});


// list chats of authenticated user.
router.post("/auth/list_chats", function(req, res) {
    // get user
    // get user's chats
    // return list of chat_ids along with the name of the other user for displaying

    // TODO IMPL
});

// on success: 
//      when new chat created: {success: true, id: [chat_id], info: "chat_created"}
//      when chat existed already: {success: true, id: [chat_id], info: "chat already existed"}
//      when group chats are implemented, users could shate multiple chats, so return a list of ids.
// on failure: {success: false, error: "could not fetch other user"}
router.post("/auth/start_chat/:name", function(req, res){
    // create a chat connection between two users
    // the first user is obtained from the token, the other
    // user is obtained by the url_param
    var self = auth.is_auth(current_token); // get the username of the sender
    user.exists(req.params, function(result){
        if(result.success)
        {
            // start chat with user, send success
            var other = req.params.name;
            // check if the chat exists:
            var shared = chatHandler.common_chat([self, other]);
            // if there is shared chat, return the chat ID.

            if(shared.length === 0){
                // if not create the chat, return chat_id
                var chat_id = chatHandler.create_chat();
                var chat = chatHandler.get(chat_id);
                chat.add_user(self);
                chat.add_user(other);
                return res.json({success: true, id: [chat_id], info: "chat_created"});
            }else{
                console.log("has shared chat");
                return res.json({success: true, id: shared, info: "chat already existed"});
            }

            return res.send("chat started between: " + self + " other: " + other);
        }
        return res.json({success: false, error: "could not fetch other user"});
    });
});

// read from chat, if get_all is true then get the entire chat
// otherwise get only the unread chat
function read(req, res, get_all){
    var self = auth.is_auth(current_token);
    var chat_id = req.params.chat_id;
    var chat = chatHandler.get(chat_id);
    if(chat)
    {
        // read from chat.
        var g = "";
        if(get_all)
            g = chat.get();
        else
            g = chat.get_unread(self);

        return res.json({success: true, chat_msgs: g, id: chat_id});
    }
    return res.json({success: false, error: "chat id does not exist"});
}

// read from chat
// return unsuccessful if the chat id does not exist
router.post("/auth/read_all/:chat_id", function(req, res){
    return read(req, res, true);
});


router.post("/auth/read/:chat_id", function(req, res){
    return read(req, res, false);
});



// write to chat
router.post("/auth/send/:chat_id", function(req, res){
    // write to chat with id
    var self = auth.is_auth(current_token);
    var chat_id = req.params.chat_id;
    var chat = chatHandler.get(chat_id);
    if(chat)
    {
        // read from chat.
        return res.json({success: chat.send(self, req.body.msg), wrote: req.body.msg, id: chat_id});
    }
    return res.json({success: false, error: "chat id does not exist"});
});



module.exports = router;
