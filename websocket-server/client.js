var io = require('socket.io-client');
var socket = io('http://localhost:3000');

setInterval(function(){
socket.emit('update', {path: 'testdb.testcollection', data: 'hello world'});
}, 2000);

function listenToPath(path, callback){
	socket.emit('listen', {path: 'testdb.testcollection'});

	socket.on(path, callback)	
}

listenToPath('testdb.testcollection', function(data){
	console.log('path fetched');
	console.log(data);
})