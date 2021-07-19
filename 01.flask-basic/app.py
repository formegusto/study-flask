from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "<h1>My First Flask Web!</h1>"


if __name__ == "__main__":
    host = "127.0.0.1"
    port = "8080"
    app.run(host=host, port=port, debug=True)
