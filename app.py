from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World. reloaded"


@app.route("/super_simple")
def super_simple():
    return jsonify(message="Hello World")
    # return jsonify(message="Hello World"), 200


@app.route("/not_found")
def not_found():
    return jsonify(message="not found"), 404
if __name__ == '__main__':
    app.run()