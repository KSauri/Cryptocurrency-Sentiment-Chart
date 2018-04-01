import os
import socketio

from flask import Flask, Response
from flask_socketio import SocketIO, send, emit
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
# establish app key
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
# set socketio
socketio = SocketIO(app)
# protect from CSRF
# csrf = CSRFProtect(app)

@app.route('/')
def healthcheck():
    return "what hell"

@app.route('/update', methods=["POST"])
def update_data():
    socketio.emit('message', {'msg': "here is my data"}, broadcast=True)
    return Response(status=200)

if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
