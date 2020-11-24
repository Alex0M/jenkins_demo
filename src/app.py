import socket
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    version = "v0.1"
    hostname = socket.gethostname()
    return "Hello, I'm {} Version: {}".format(hostname, version)

if __name__ == '__main__':
    app.run(debug=True)
