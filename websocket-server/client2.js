var baas = require('./client-lib');

var token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJwYXNzd29yZCI6IjEyMyIsImVtYWlsIjoiZXNzYW0iLCJfaWQiOnsiJG9pZCI6IjVhY2JiNmJhN2Y3OGIxMGZmMmRjODEyNiJ9fQ.zhcvC1RjxZcYMPcss2c-by1Fn4u-xpU5nFVNPTE-W8I';

baas.listen("sessiondb.comedyMovies", token, function(response){
	console.log(response);
})

setTimeout(function(){
	baas.update("sessiondb.comedyMovies", token, {name: 'updated data'}, {name: 'reupdated, data'})
}, 3000);