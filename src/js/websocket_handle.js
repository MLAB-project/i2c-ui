function WebSocketTest()
{
	if ("WebSocket" in window)
	{
		var ws = new WebSocket("ws://"+window.location.hostname+":"+window.location.port+"/rt/");
		var sensors = [];
		var startTime = 0;

		ws.onopen = function()
		{
			ws.send("Hello its me");
			startTime = (new Date()).getTime()

		};

		ws.onmessage = function (evt) 
		{ 
			var received_msg = evt.data;
			console.log(received_msg);
			var data = received_msg.split(';');

			if (data[0]=="$rtdt"){
				var chart = $('#container').highcharts();

				if (sensors.indexOf(data[1]) > -1){
					console.log( "LOG: " + sensors.indexOf(data[1]) )
				}
				else{
					console.log("To byl novy sensor - "+data[1]+ " uz mam " +chart.series);
					chart.addSeries({
                		name : data[1],
                		data : (function () {
                    		var data = [], time = (new Date()).getTime();
                    		data.push([ startTime , 0 ]);
                    		return data;
                		}())
                	})
					sensors.push(data[1]);
				}

				var x = (new Date()).getTime(), y = data[3]*1;
				chart.series[sensors.indexOf(data[1])+1].addPoint([x, y], true, false);
			}
		};

		ws.onclose = function()
		{ 
			alert("Connection is closed... try it reload"); 
		};
	}

	else
	{
		alert("WebSocket NOT supported by your Browser!");
	}
}