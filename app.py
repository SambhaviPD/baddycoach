from flask import Flask

import random
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/configure-input', methods=['POST'])
def configure_input():
    pass

@app.route('/send-instruction', methods=['GET'])
def send_instruction():
    pass