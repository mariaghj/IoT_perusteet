const WebSocket = require('ws');

const server = new WebSocket.Server({port: 8800})

server.on('connection', socket => {
    console.log('Yhteys avattu');

    socket.on ('message', message => {
        console.log('Received: ' + message.toString());
        socket.send(`Echo: ${message}`);
    });
    socket.on('close', () => {
        console.log('Yhteys suljettu');
    })
});