var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var axios = require('axios');

let sockets = {};
let listenPaths = {};

io.on('connection', function(socket){
	sockets[socket.id] = socket;
	socket.on('disconnect', function(){
		console.log('removing ' + socket.id);
		delete sockets[socket.id];
	});
	socket.on('listen', function(data){
		if(listenPaths[data.path])
			listenPaths[data.path].push(socket.id);
		else
			listenPaths[data.path] = [socket.id];
		emitToPath(data.path, {});
	})

	socket.on('update', function(data){
		emitToPath(data.path)
	})
});

function emitToPath(path, condition){
	let pathArray = path.split('.');
	let dbname = pathArray[0];
	let collection = pathArray[1];

	axios.get('http://localhost:5000/findCondition', {params: {dbname, collection, condition}, headers: {AUTHTOKEN: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6IjEyMyIsImVtYWlsIjoiZXNzYW0iLCJfaWQiOnsiJG9pZCI6IjVhY2JiNmJhN2Y3OGIxMGZmMmRjODEyNiJ9fQ.zhcvC1RjxZcYMPcss2c-by1Fn4u-xpU5nFVNPTE-W8I'}}).then(function(response){
		console.log(response.data);
		let ids = listenPaths[path];
		ids.map(function(id){
			let client = sockets[id];
			//update the database here
			if(client)
				client.emit(path, response.data);
		});
	})
}

http.listen(3000, function(){
  console.log('listening on localhost:3000');
});