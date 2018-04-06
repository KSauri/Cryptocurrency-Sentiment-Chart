import os
import json

from flask import Flask, Response
from flask_socketio import SocketIO
from collections import deque

app = Flask(__name__)
# establish app key
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
# set socketio
socketio = SocketIO(app)
# set the max length of data - this set how many data points each graph will have
MAX_LEN = 864

# set Reddit deque object
reddit_data = deque(maxlen=MAX_LEN) 
# set Crypto deque object
crypto_data = deque(maxlen=MAX_LEN)


@socketio.on('connect')
def send_current_data():
    current_data = json.dumps(dict(
        reddit=list(reddit_data),
        crypto=list(crypto_data),
        maxLen=MAX_LEN
    ))
    socketio.emit('connect_response', current_data)


@app.route('/')
def healthcheck():
    return "what's up"


@app.route('/reddit', methods=["POST"])
def update_reddit_data(data):
    # update the current state of data
    reddit_data.append(data)
    # update clients with newest piece of data
    reddit_data_json = json.dumps({"reddit": data})
    socketio.emit('reddit', reddit_data_json, broadcast=True)
    return Response(status=200)


@app.route('/crypto', methods=["POST"])
def update_crypto_data(data):
    # update the current state of data
    crypto_data.append(data)
    # update clients with newest data
    crypto_data_json = json.dumps({"crypto": data})
    socketio.emit('crypto', crypto_data_json, broadcast=True)
    return Response(status=200)


if __name__ == '__main__':
    socketio.run(app, debug=True, host="0.0.0.0")
