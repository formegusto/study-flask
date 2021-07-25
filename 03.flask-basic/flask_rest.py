from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/json_test")
def json_test():
    data = {
        "name": "노팀장",
        "department": "dev"
    }
    return jsonify(data)


@app.route("/json_test_2")
def json_test_2():
    data = ["노팀장", "노대표", "노사원"]
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
