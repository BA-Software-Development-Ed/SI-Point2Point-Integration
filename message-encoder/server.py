from flask import Flask, request
import os
import signal

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():

    if request.method == 'POST':
        response = request.data.decode('utf-8')
        if response == 'stop':
            os.kill(os.getpid(), signal.SIGINT)
            return 'Server terminated!'
        else:
            return response
    return 'Send a POST request with some text or \'stop\' to terminate the server'


app.run(port=6666, threaded=True, debug=True)
