window.onload = function () {

var dataPoints = [];

var chart = new CanvasJS.Chart("chartContainer", {
	animationEnabled: true,
	theme: "light2", // "light1", "light2", "dark1", "dark2"
	exportEnabled: true,
	title: {
		text: "tick"
	},
	axisX: {
		interval: 1,
		valueFormatString: "MMM"
	},
	axisY: {
         stripLines:[
            {
                
                startValue:90,
                endValue:100,                
                color:"#A5FF33",
            }
            ],
		prefix: "$",
		title: "Price"
	},
	// toolTip: {
	// 	content: "Date: {x}<br /><strong>Price:</strong><br />Open: {y[0]}, Close: {y[3]}<br />High: {y[1]}, Low: {y[2]}"
	// },
	data: [{
		type: "candlestick",
		yValueFormatString: "$##0.00",
		dataPoints: dataPoints
	}]
});

chart.render();

$.get("https://canvasjs.com/data/gallery/javascript/netflix-stock-price.csv", getDataPointsFromCSV);
let counter = 0
function getDataPointsFromCSV(csv) {
	var csvLines = points = [];
	csvLines = csv.split(/[\r?\n|\r|\n]+/);
	console.log(csv)
	for (var i = 0; i < csvLines.length; i++) {
		if (csvLines[i].length > 0) {
			points = csvLines[i].split(",");
			console.log(csvLines[i])
			dataPoints.push({
				x: new Date(
					parseInt(points[0].split("-")[0]),
					parseInt(points[0].split("-")[1]),
					parseInt(points[0].split("-")[2])
				),
				y: [
					parseFloat(points[1]),
					parseFloat(points[2]),
					parseFloat(points[3]),
					parseFloat(points[4])
				]
			});
		}

	chart.render();
}

var updateChart = function () {

	// var csvLines = points = [];
	// csvLines = csv.split(/[\r?\n|\r|\n]+/);
	// for (var i = 0; i < csvLines.length; i++) {
	// 	if (csvLines[i].length > 0) {
	// 		points = csvLines[i].split(",");

	points = ["2016-00-25,99.779999,102.680000,90.110001,91.839996"]
			dataPoints.push({
				x: new Date(
					parseInt(points[0].split("-")[0]),
					parseInt(points[0].split("-")[1]),
					parseInt(points[0].split("-")[2])
				),
				y: [
					parseFloat(points[1]),
					parseFloat(points[2]),
					parseFloat(points[3]),
					parseFloat(points[4])
				]
			});
		// }
	// }
	chart.render();
	};

	// update chart every second
	setInterval(function(){updateChart()}, 1000);
}
