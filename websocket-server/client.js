var io = require('socket.io-client');
var socket = io('http://localhost:3000');

// setInterval(function(){
// socket.emit('update', {path: 'testdb.testcollection', data: 'hello world'});
// }, 2000);
var token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6IjEyMyIsImVtYWlsIjoiZXNzYW0iLCJfaWQiOnsiJG9pZCI6IjVhY2JiNmJhN2Y3OGIxMGZmMmRjODEyNiJ9fQ.zhcvC1RjxZcYMPcss2c-by1Fn4u-xpU5nFVNPTE-W8I';

function listenToPath(path, callback){
	socket.emit('listen', {path: path, token: token});

	socket.on(path, function(data){
		if(data.code != 1)
			console.error(data.message)
		else
			callback(data.message);
	})
}

function insert(path, data){
	socket.emit('insert', {path: path, token: token, obj: data});
}

function remove(path, data){
	socket.emit('remove', {path: path, token: token, condition: data});
}

function update(path, condition, data){
	socket.emit('update', {path: path, token: token, condition: condition, data: data});
}

listenToPath('sessiondb.comedyMovies', function(data){
	console.log('path fetched');
	console.log(data);
})

setTimeout(function(){
	update('sessiondb.comedyMovies', {name: "the hangover"}, {name: 'updated by websocket'});
}, 3000);