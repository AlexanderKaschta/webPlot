from flask import Flask
from flask_socketio import SocketIO

# Create an instance
app = Flask("webPlot", static_folder='static', static_url_path='/static')
# Secret key for encryption, change it for a production deployment
app.config['SECRET_KEY'] = 'DasIstEinSuperSichererSchl├╝sselF├╝rDieVerschl├╝sselung!'

# Init the Socket.IO
socketio = SocketIO(app)
