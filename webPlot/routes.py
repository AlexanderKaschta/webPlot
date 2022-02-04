import multiprocessing as mp

from flask import render_template

import webPlot.daq
from webPlot import app, socketio, processes, data_queue


@app.route('/')
def index():
    return render_template('index.jinja2', title="Home")


@app.route('/config')
def config():
    return render_template('config.jinja2', title="Config")


@app.route('/plot')
def plot():
    return render_template('plot.jinja2', title="Plot")


# Methode to start the data acquisition
@app.route('/start')
def start():
    processes.append(mp.Process(name="Data acquisition process", target=webPlot.daq.startDAQ, args=(data_queue,)))
    for prc in processes:
        # Start all processes, that haven't started yet
        if not prc.is_alive():
            prc.start()
            print('Starting subprocess ', prc.name, ' PID=', prc.pid)
    return "Started!"


# Methode to stop the data acquisition
@app.route('/stop')
def stop():
    # Shut-down all sub-process(es)
    for p in processes:
        if p.is_alive():
            p.terminate()
            processes.remove(p)
            print('Terminating ' + p.name)
    return "Stopped!"


@app.route('/test')
def test():
    data = {"x": 0, "y": 5}
    socketio.emit("data", data, json=True)
    return "Test"
