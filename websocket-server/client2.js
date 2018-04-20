var io = require('socket.io-client');
var socket = io('http://localhost:3000');

setInterval(function(){
socket.emit('update', {path: 'testdb2.testcollection2', data: 'hello world'});
}, 2000);

function listenToPath(path, callback){
	socket.emit('listen', {path: path});

	socket.on(path, callback)	
}

listenToPath('testdb2.testcollection2', function(data){
	console.log('path fetched');
	console.log(data);
})