const express = require("express");
const server = express();

server.use("/", express.static(__dirname + '/build'));

const port = process.env.PORT || 3000;

console.info("Listen port: "+ port);
server.listen(port);
