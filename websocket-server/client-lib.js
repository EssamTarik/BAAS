module.exports=baas;
//var http = require('http');
//var io = require('socket.io')(http);
var util = require('util');
var events = require('events');
var io = require('socket.io-client');
const socket = io('http://localhost');


//util.inherts(baas,io);
//util.inherts(baas,http);
util.inherits(baas,events);
//util.inherits(baas,io);


function baas() {

	this.listen= function(path,callback,token,data) {
	
	socket.on(path,,function(path){
		
		//i think we should make an event for the token and i emit it here and send me back data.code and i use it every time to verify the action so i will do it like this 
		
		
		callback(path);
	});

	socket.emit("listen",{path:path,token:token});

};
	this.insert= function(path,token,obj){
		socket.emit('insert',{path:path,token:token,obj:obj});
	};


 


	this.remove=function(path,obj,*condition????,token){
		socket.emit('remove',{path:path,obj:obj,token:token,condition:condition});

	};



	this.delete=function(path,obj,*condition????,token){
		socket.emit('delete',{path:path,obj:obj,token:token,condition:condition});

	};



	this.update=function(path,obj,*condition????,token){
		socket.emit('update',{path:path,obj:obj,token:token,condition:condition});

	};

};



