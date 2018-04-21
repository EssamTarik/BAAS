var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var axios = require('axios');
var config = require('./config');

let sockets = {};
let listenPaths = {};

function findCondition(data, condition, callback){
	let pathArray = data.path.split('.');
	let dbname = pathArray[0];
	let collection = pathArray[1];

	axios.get(config.BackendURL + '/findCondition', {params: {dbname, collection, condition}, headers: {AUTHTOKEN: data.token}}).then(function(response){
		callback(data.path, response.data);
	}).catch(function(error){
		emitToSocket(data.socket, data.path, error.response.data);
	})
}

function insert(data, obj, callback){
	let pathArray = data.path.split('.');
	let dbname = pathArray[0];
	let collection = pathArray[1];
	var params = {dbname, collection, data: obj};
	axios.get(config.BackendURL + '/insert', {params , headers: {AUTHTOKEN: data.token}}).then(function(response){
		console.log(response.data);
		callback();
	}).catch(function(error){
		emitToSocket(data.socket, data.path, error.response.data);
	})
}

io.on('connection', function(socket){
	sockets[socket.id] = socket;
	socket.on('disconnect', function(){
		console.log('removing ' + socket.id);
		delete sockets[socket.id];
	});
	socket.on('listen', function(data){
		console.log(socket.id + ' is listening');
		if(listenPaths[data.path])
			listenPaths[data.path].push(socket.id);
		else
			listenPaths[data.path] = [socket.id];
		findCondition({path: data.path, socket: socket, token: data.token}, {}, emitToPath);
	})

	socket.on('insert', function(data){
		data.socket = socket;
		insert(data, data.obj, function(){
			findCondition(data, {}, emitToPath);
		});
	})
});

function emitToPath(path, data){
	let ids = listenPaths[path];
	ids.map(function(id){
		let client = sockets[id];
		//update the database here
		if(client)
			client.emit(path, data);
	});
}

function emitToSocket(socket, path, data){
	socket.emit(path, data);
}


http.listen(3000, function(){
  console.log('listening on localhost:3000');
});