function Chat(){
	this.users = [];
	this.msgs = [];
	this.callback = null;
}

// add a user to the chat
Chat.prototype.add_user = function(user){
	this.users.push(user);
};

// send a msg to the chat, true if msg has been sent, false otherwise.
Chat.prototype.send = function(user, txt){
	if(this.is_member(user)){
		var msg_to_send = {msg: txt, read_by: [], time: "LOCAL TIME", sender: user}; 
		this.msgs.push(msg_to_send);
		// run the callback
		if(this.callback)
			this.callback(msg_to_send);
		return true; // sent
	}
	return false;
};

// get the entire chat in the form of: [{msg: theMsg, sent_by: theSender, time: theSendTime}, ...]
Chat.prototype.get = function(){
	var m = [];
	for(var i = 0; i < this.msgs.length; i++){
		var item = this.msgs[i];
		m.push({msg: item.msg, sent_by: item.sender, time: item.time});
	}
	return m; // all msgs without user data and time
};

// get only the unread chat of a user.
// return an object array format: [{msg: theMsg, sent_by: theSender, time: theSendTime}, ...]
// if 'by' is not a memebr of the chat, return false.
Chat.prototype.get_unread = function(by){
	if(!this.is_member(by))
		return false;
	var m = [];
	for(var i = 0; i < this.msgs.length; i++){
		var item = this.msgs[i];
		var readers = item.read_by;
		if(readers.indexOf(by) === -1)
		{
			// item is not read by the user
			m.push({msg: item.msg, sent_by: item.sender, time: item.time});
			// add the user to the read list.
			this.msgs[i].read_by.push(by);
		}
	}
	return m;
};

// check if the user is a member of this chat
Chat.prototype.is_member = function(user){
	return this.users.indexOf(user)  > -1; 
};

Chat.prototype.set_callback = function(callback){
	this.callback = callback;
};

//===========================================
//----------------CHAT HANDLER---------------
//===========================================

// initalize the chat handler
function ChatHandler () {
	this.chats = {};
	this.last_id = 0;
}

// create a chat
ChatHandler.prototype.create_chat = function(){
	var id = this.last_id;
	this.last_id++;
	this.chats[id] = new Chat();
	return id;
};

// get the chat with the id 'id'
ChatHandler.prototype.get = function(id){
	return this.chats[id];
};

// reutrn all chats in which 'user' is a member as an array of ids
ChatHandler.prototype.get_chats_with_user = function(user){
	var keys = Object.keys(this.chats);
	var m = [];
	for(var i = 0; i < keys.length; i++){
		var key = keys[i];
		var chat = this.chats[key];
		if(chat.is_member(user))
			m.push(key);
	}
	return m;
};

// get a list of ids of shared chats of [users]
ChatHandler.prototype.common_chat = function(users){
	var shared = [];
	var keys = Object.keys(this.chats);
	// check each chat.
	for(var i = 0; i < keys.length; i++){
		var key = keys[i];
		var val = this.chats[key]; // the chat
		var shares = true;
		// check if each user is a member of the chat
		for(var member = 0; member < users.length; member++){
			//console.log("chekcing if " + users[member] + " is a member ... result: " + val.is_member(users[member]));
			if(!val.is_member(users[member])){
				shares = false;
				break;
			}
		}
		if(shares)
			shared.push(key);
	}
	console.log(":: SHARED ::");
	console.log(shared);
	return shared;
};

ChatHandler.prototype.get_group_chat = function(){
	return this.chats[0]; // group chat is always the first one to be created.
};

var handler = new ChatHandler();
handler.create_chat(); // creates the group chat.

module.exports = handler;

