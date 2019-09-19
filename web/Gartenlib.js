///////////////////////////////////////////////////////////////////
function onopen() {
	console.log("opened! Sending: "+data);
    socket.send(data);
}

function onclose() {
     // websocket is closed.
     console.log("Connection closed...");
	 
 };

// Log errors
function onerror(error) {
  console.log('WebSocket Error ' + error);
};

function OpenSocket(onMessageHandler) {
	var ws = new WebSocket('ws://'+ipSocketServer+':'+portSocketServer);
	ws.onopen = onopen;
	ws.onmessage =onMessageHandler; 
	ws.onclose = onclose;
	ws.onerror =onerror ;
	return ws;
}
