var User = require("../models/user");


var exports = {
	create_user : function(userObj, callback)
	{
	var username = userObj.name;
	var mail = userObj.email;
	var password = userObj.password;
	// note: password hashing is done in the user scheme
	if(!username || !mail || !password) 
		return callback({success: false, error: "incomplete form"});
	// attempt to create user
	
	var newUser = new User({
      name: username,
      password: password,
      email_addr: mail
    });

	newUser.save(function(err){
		var is_err = err ? false : true;
		return callback({success: is_err, error: "user already exists"});
	});
	},

	delete_user : function(userObj, callback)
	{
		var username = userObj.name;
		User.findOne(
			{name: username},
			function(err) {
				if(err)
					return callback({success: false, error: err, msg: "user not deleted / doesnt exist"});
			}).remove(function(err) {
				return callback({success: err ? false : true, error: err, msg: err ? "user not deleted" : "user deleted"});
		});
	},

	update_user : function(userObj, callback)
	{
		callback(undefined);
	},

	get_user : function(userObj, callback)
	{
		var username = userObj.name;
		var password = userObj.password;
		User.findOne(
			{ name: username },
			function(err, user) {
				if(err || !user)
					return callback({success: false, error: 'Authentication failed. password or username is incorrect' });
	      		// check if password matches
	      		user.comparePassword(password, function (err, isMatch) {
	      				var isValid = !(isMatch && !err)
	      				callback({success: isValid , error: isValid ? "" : "Authentication failed. password or username is incorrect"});
	      		});
	    	});
	},

	exists : function(userObj, callback)
	{
		var username = userObj.name;
		User.findOne({}, function (err, user) {
			if(err)
				return callback({success: false, error: "user doesnt exits"});
			return callback({success: true});
		});
	}
};

module.exports = exports;

function show_user(username, password, callback)
{

}