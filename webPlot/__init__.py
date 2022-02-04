from flask import Flask
from flask_socketio import SocketIO
import multiprocessing as mp

# Create an instance
app = Flask("webPlot", static_folder='static', static_url_path='/static')
# Secret key for encryption, change it for a production deployment
app.config['SECRET_KEY'] = 'DasIstEinSuperSichererSchlüsselFürDieVerschlüsselung!'

processes = []
data_queue = mp.Queue(1)

# Init the Socket.IO
socketio = SocketIO(app)

from webPlot.routes import *
from webPlot.webSocket import *
