function WebSocketTest()
{
	if ("WebSocket" in window)
	{
		//alert("WebSocket is supported by your Browser!");

		// Let us open a web socket
		var ws = new WebSocket("ws://telescope.local:8888/rt/");

		ws.onopen = function()
		{
			// Web Socket is connected, send data using send()
			ws.send("Message to send");
			//alert("Message is sent...");
		};

		ws.onmessage = function (evt) 
		{ 
			var received_msg = evt.data;
			//alert("Message is received..."+received_msg);
			var data = received_msg.split(';');

			if (data[1] == "Teplota01") {
				var chart = $('#container').highcharts();
				var x = (new Date()).getTime(), y = data[3]*1;
				chart.series[0].addPoint([x, y], true, false);
				console.log("A");
			};
			if (data[1] == "Teplota02") {
				var chart = $('#container').highcharts();
				var x = (new Date()).getTime(), y = data[3]*1;
				chart.series[1].addPoint([x, y], true, false);
				console.log("B");
			};
			if (data[1] == "vlhkost") {
				var chart = $('#container').highcharts();
				var x = (new Date()).getTime(), y = data[3]*1;
				chart.series[2].addPoint([x, y], true, false);
				console.log("C");
			};
		};

		ws.onclose = function()
		{ 
			// websocket is closed.
			alert("Connection is closed..."); 
		};
	}

	else
	{
		// The browser doesn't support WebSocket
		alert("WebSocket NOT supported by your Browser!");
	}
}