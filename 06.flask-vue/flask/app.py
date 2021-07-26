from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test")
def get_test():
    test_item = {
        "name": "th",
        "age": 26
    }
    return jsonify(test_item)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
