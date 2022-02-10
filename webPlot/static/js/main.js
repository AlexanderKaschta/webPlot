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
    margin: {t: 80},
    showlegend: true,
};

var socket = io({transports: ['websocket']});
socket.on('connect', function () {
    socket.emit('connected', {client: 1});
});

socket.on('error', console.error.bind(console));

Plotly.newPlot("plot", [{x: [], y: [], name: "Messung"}], layout, config);

socket.on('x-axis', function (data) {

    var update = {
        'xaxis.title.text': data.title + " (" + data.unit + ")",
    };

    Plotly.relayout("plot", update)
});

socket.on('y-axis', function (data) {

    var update = {
        'yaxis.title.text': data.title + " (" + data.unit + ")",
    };

    Plotly.relayout("plot", update)
});

socket.on('data', function (data) {
    // Log the transferred data
    console.log(data);

    var time = new Date();

    var update = {
        x: [[new Date(data.time * 1000)]],
        y: [[data.data[0]]]
    }

    var olderTime = time.setMinutes(time.getMinutes() - 1);
    var futureTime = time.setMinutes(time.getMinutes() + 1);

    var minuteView = {
        xaxis: {
            type: 'date',
            range: [olderTime, futureTime]
        }
    };

    Plotly.relayout("plot", minuteView);

    Plotly.extendTraces("plot", update, [0])
});

