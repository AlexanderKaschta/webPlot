from webPlot import socketio, data_queue


@socketio.on('connected')
def connected(json):
    print('A new client connected: ' + str(json))


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))


def check_for_data():
    while not data_queue.empty():
        a = data_queue.get()
        socketio.emit("data", a, json=True)
        print(a)
