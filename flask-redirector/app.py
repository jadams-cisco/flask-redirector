
from waitress import serve
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/background')
def background():
    return app.send_static_file('background.jpg')

serve(app, listen='*:8080')