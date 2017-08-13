const express = require("express");
const server = express();

server.use("/", express.static(__dirname + '/build'));

server.get('*', (req, res) => {
  res.sendFile(__dirname + '/build/index.html');
});

const port = process.env.PORT || 3000;

console.info("Listen port: "+ port);
server.listen(port);
