//var http = require('http');
//var io = require('socket.io')(http);
var util = require('util');
var events = require('events');
var io = require('socket.io-client');
const socket = io('http://localhost:3000');


//util.inherts(baas,io);
//util.inherts(baas,http);
//util.inherits(baas,events);
//util.inherits(baas,io);


const baas = {

	listen: function(path, token, callback) {
		socket.on(path,function(data){
			callback(data);
		});
		socket.emit("listen",{path:path,token:token});
	},

	insert: function(path,token,obj){
		socket.emit('insert',{path:path,token:token,obj:obj});
	},

	remove: function(path, token, condition){
		socket.emit('remove',{path:path, token:token, condition:condition});

	},

	update: function(path, token, condition, data){
		socket.emit('update',{path:path,token:token,condition:condition, data:data});
	},

};



module.exports=baas;