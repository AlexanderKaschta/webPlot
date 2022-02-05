from webPlot import app, socketio

# Start the application
# For public deployment of the development server add host='0.0.0.0'
socketio.run(app, host='0.0.0.0', debug=True)
