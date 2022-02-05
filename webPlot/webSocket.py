from webPlot import socketio


@socketio.on('connected')
def connected(json_data):
    if "type" in json_data:
        print("A new sensor connected: " + str(json_data))
    else:
        print('A new client connected: ' + str(json_data))


@socketio.on('new-data')
def handle_my_custom_event(data):
    print('received json: ' + str(data))
    socketio.emit("data", data, json=True)
