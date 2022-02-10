from webPlot import socketio


@socketio.on('connected')
def connected(json_data):
    if "type" in json_data:
        print("A new sensor connected: " + str(json_data))
    else:
        print('A new client connected: ' + str(json_data))


@socketio.on('new-data')
def handle_new_data(data):
    print('received json: ' + str(data))
    socketio.emit("data", data, json=True)


@socketio.on('axis')
def handle_axis_event(data):
    if data["index"] == 1:
        socketio.emit("x-axis", {"title": "Time", "unit": "Timestamp"}, json=True)
        socketio.emit("y-axis", {"title": data["label"], "unit": data["unit"]}, json=True)
