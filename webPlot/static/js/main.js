// Define the plot config
const config = {responsive: true, locale: 'de', displaylogo: false};

const layout = {
    title: "Test-Plot",
    font: {size: 16},
    margin: {t: 80}
};

var socket = io();
socket.on('connect', function () {
    socket.emit('connected', {data: 'I\'m connected!'});
});

socket.on('error', console.error.bind(console));

Plotly.newPlot("plot", [{x: [], y: []}], layout, config);

socket.on('data', function (data) {
    // Log the transferred data
    console.log(data);

    var time = new Date();

    var update = {
        x:  [[time]],
        y: [[data.y]]
    }

    Plotly.extendTraces("plot", update, [0])
});

