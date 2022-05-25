const http = require('http');
const express = require('express');
const path = require('path');
const app = express();
var server = http.createServer(app);
var io = require('socket.io').listen(server);//Passing server instance

const port =3836 //Port Number

app.use('/static', express.static('public'));

server.listen(port, ()=>{
  console.log(`Server is running on port: ${port}`)
});

app.get('/', function(req, res){
  console.log("Homepage")
  res.sendFile(path.join(__dirname, '/index.html'))
});

io.sockets.on('connection', function(socket){
  console.log("Socket connected succesfully....");

  socket.on("test", function(data){
    console.log(data);
  });
  
  socket.on("soil", function(data){
    console.log(data);
  });
})
