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
            var chart = $('#container').highcharts();
            var received_msg = evt.data;
            console.log(received_msg);
            var data = received_msg.split(';');

            if (data[0]=="$hello"){
                for (var i = data[1]*2 - 1; i >= 0; i--) {
                    //console.log("To byl novy sensor - "+data[i+2]+ " s id: "+ i);
                    chart.addSeries({
                        id   : 'raw',
                        name : 'data',
                        data : (function () {
                            var data = [], time = (new Date()).getTime();
                            data.push([ startTime , 0 ]);
                            return data;
                        }())
                    })
                    sensors.push(data[i+2]);
                };
                sensors=sensors.sort();
                console.log(sensors);
                //for (var i = sensors.length - 1; i >= 0; i--) {
                //  console.log( sensors[i] + "  " + chart.series[i])
                //};
            }

            if (data[0]=="$rtdt"){
                if (sensors.indexOf(data[1]) < 0){
                    //console.log( "LOG: " data[1]+ " je: " + sensors.indexOf(data[1]));
                }

                var x = (new Date()).getTime(), y = data[3]*1;
                //var series = chart.get('raw');
                //console.log(series.name)
                //var x = data[2]*1, y = data[3]*1;
                //chart.series[sensors.indexOf(data[1])].addPoint([x, y], true, false);
                //console.log("add to:"+ data[4] + chart.series[data[4]].name)
                chart.series[data[4]*2].addPoint([x, y], true, false);
                chart.series[data[4]*2].name = data[1];
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