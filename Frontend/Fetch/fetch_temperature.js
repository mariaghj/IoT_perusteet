// Load Google Charts
google.charts.load('current', { packages: ['corechart'] });


function drawChart() {
    const feeds = window.temperatures || [];
    if (!feeds || feeds.length === 0) return;

    const chartData = new google.visualization.DataTable();
    chartData.addColumn('datetime', 'Time');
    chartData.addColumn('number', 'Temperature (°C)');

    feeds.forEach(item => {
        const time = new Date(item.time);
        const temp = parseFloat(item.temp);
        if (!isNaN(temp)) chartData.addRow([time, temp]);
    });

    const options = {
        title: 'Temperature Over Time',
        height: 500,
        legend: { position: 'bottom' },
        areaOpacity: 0.3,
        hAxis: { title: 'Time', format: 'dd.MM HH:mm' },
        vAxis: { title: 'Temperature (°C)' },
        interpolateNulls: true
    };

    const chart = new google.visualization.AreaChart(document.getElementById('chart_div'));
    chart.draw(chartData, options);
}


const url = "https://api.thingspeak.com/channels/3083020/feeds.json?api_key=1491X9T2I5AC9LI5";

fetch(url)
.then(response => response.json())
.then(data => {
    const feeds = data.feeds;
    const temperatures = feeds.map(Feed => ({
        time: Feed.created_at,
        temp: parseFloat(Feed.field1)
    }));

    window.temperatures = temperatures;


    document.getElementById("output").textContent = JSON.stringify(temperatures, null, 2);
    google.charts.setOnLoadCallback(drawChart);
})

.catch(error => {
    console.error('Error fetching data:', error);
    document.getElementById("output").textContent = "Error loading data.";
});