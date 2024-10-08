from flask import Flask, send_from_directory

import os

app = Flask(__name__)

@app.route("/")
def test():
    return "<p>test</p><h1>TEST</h1>"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')
