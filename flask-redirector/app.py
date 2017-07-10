
from waitress import serve
from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''}, methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
@app.route('/<path:path>', methods=['GET', 'PUT', 'POST', 'PATCH', 'DELETE'])
def index(path):
    return app.send_static_file('index.html')

@app.route('/background')
def background():
    return app.send_static_file('background.jpg')

serve(app, host="0.0.0.0", port='8080')
