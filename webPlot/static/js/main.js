// Define the toggle button

var toggle = document.getElementById('toggle');

var running = false;

toggle.addEventListener("click", function () {
    // Make the matching network request in the background
    let xhr = new XMLHttpRequest();
    if (running) {
        xhr.open('GET', '/stop', true);
        toggle.classList.remove("active");
    } else {
        xhr.open('GET', '/start', true);
        toggle.classList.add("active");
    }
    xhr.send(null);

    // Invert the running state
    running = !running;
});


// Define the plot config
const config = {responsive: true, locale: 'de', displaylogo: false};

const layout = {
    title: "Test-Plot",
    font: {size: 16},
    margin: {t: 80}
};

var socket = io();
socket.on('connect', function () {
    socket.emit('connected', {client: 1});
});

socket.on('error', console.error.bind(console));

Plotly.newPlot("plot", [{x: [], y: []}], layout, config);

socket.on('data', function (data) {
    // Log the transferred data
    console.log(data);

    var update = {
        x:  [[data.time]],
        y: [[data.data]]
    }

    Plotly.extendTraces("plot", update, [0])
});

