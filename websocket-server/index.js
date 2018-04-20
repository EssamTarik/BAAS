var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.send('<h1>Hello world</h1>');
});

let sockets = {};
let listenPaths = {};

let db = {'testdb.testcollection': 'first test data', 'testdb2.testcollection2': 'second test data'};

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
	})
	socket.on('update', function(data){
		console.log(Object.keys(sockets));
		let ids = listenPaths[data.path];
		ids.map(function(id){
			let client = sockets[id];
			//update the database here
			if(client)
				client.emit(data.path, db[data.path]);

		});
	})
});

// setTimeout(function(){
// 	let id = listenPaths['testdb.testcollection'];
// 	let client = sockets[id];
// 	client.emit('message', 'for your eyes only');	
// }, 2000);

http.listen(3000, function(){
  console.log('listening on localhost:3000');
});