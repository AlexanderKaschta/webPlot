from webPlot import app, socketio
from webPlot.webSocket import check_for_data

# Start the application
# For public deployment of the development server add host='0.0.0.0'
socketio.run(app, host='0.0.0.0', debug=True)

# Start the loop to check for new data
check_for_data()
