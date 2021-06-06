from flask import Flask, jsonify, request

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

@app.route("/parameters")
def parameters():
    name = request.args.get("name")
    age = int(request.args.get("age"))
    if age < 18:
        return jsonify(message="{} you are not old enough".format(name))
    else:
        return jsonify(message="Welcome {}".format(name))


@app.route("/url_variables/<string:name>/<int:age>")
def url_variables(name:str, age:int):
    if age < 18:
        return jsonify(message="{} you are not old enough".format(name)), 401
    else:
        return jsonify(message="Welcome {}".format(name))


if __name__ == '__main__':
    app.run()