//var http = require('http');
//var io = require('socket.io')(http);
var util = require('util');
var events = require('events');
var io = require('socket.io-client');


//util.inherts(baas,io);
//util.inherts(baas,http);
//util.inherits(baas,events);
//util.inherits(baas,io);


const baas = {
	
	initialize: function(address, token){
		this.socket = io(address);
		this.token = token;
	},

	listen: function(path, callback) {
		this.socket.on(path,function(data){
			callback(data);
		});
		this.socket.emit("listen",{path: path, token: this.token});
	},

	insert: function(path, obj){
		this.socket.emit('insert',{path: path, token: this.token, obj: obj});
	},

	remove: function(path, condition){
		this.socket.emit('remove',{path: path, token: this.token, condition: condition});

	},

	update: function(path, condition, data){
		this.socket.emit('update',{path: path, token: this.token, condition: condition, data:data});
	},

};

module.exports=baas;