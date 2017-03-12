from flask import Flask, request, jsonify, render_template, send_file
from os import system
from flask_cors import CORS, cross_origin
import requests
import threading
import atexit
import time
import sys
from actions import exec_command

data = {
    'action': False,
    'thread': None,
    # how long to wait to move the mouse to prevent standby mode? (seconds)
    'sleep': 240
}

app = Flask(__name__)
CORS(app, resources={'/api/*': {'origins': '*'}})

@app.route('/')
def index():
    r = requests.get(
        'https://watson-speech.mybluemix.net/api/speech-to-text/token',
        headers={'referer': 'https://watson-speech.mybluemix.net/microphone-streaming.html'}
    )
    return render_template('index.html', token=r.text)

@app.route('/manifest.json')
def manifest():
    return send_file('static/manifest.json')

@app.route('/favicon.ico')
def favicon():
    return send_file('static/favicon.ico')

@app.route('/api/action', methods=['GET', 'POST'])
def action():
    data['action'] = True
    command = request.args.get('command', '')
    if not command:
        command = request.form.get('command', '')
    c = exec_command(command)
    data['action'] = False
    return jsonify({'success': c})

def poll():
    # prevent that the computer sleeps
    cmd = 'xdotool mousemove_relative 15 0'
    if not data['action']:
        system(cmd)
    else:
        # retry
        time.sleep(10)
        if not data['action']:
            system(cmd)
    # next thread
    data['thread'] = threading.Timer(data['sleep'], poll, ())
    data['thread'].start()

def cleanup():
    if data['thread']:
        data['thread'].cancel()

def init():
    atexit.register(cleanup)
    data['thread'] = threading.Timer(data['sleep'], poll, ())
    data['thread'].start()

if __name__ == '__main__':
    init()
    app.run(host='0.0.0.0', port=8080)
