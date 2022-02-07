from flask import render_template

from webPlot import app, socketio


@app.route('/')
def index():
    return render_template('index.jinja2', title="Home")


@app.route('/config')
def config():
    return render_template('config.jinja2', title="Config")


@app.route('/plot')
def plot():
    return render_template('plot.jinja2', title="Plot")


@app.route('/start')
def start():
    socketio.emit("start")
    return "Send start"


@app.route('/stop')
def stop():
    socketio.emit("stop")
    return "Send stop"


@app.route('/test')
def test():
    data = {"x": 0, "y": 5}
    socketio.emit("data", data, json=True)
    return "Test"
