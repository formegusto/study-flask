from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>This is Root!</h1>"


@app.route("/hello")
def hello_flask():
    return "<h1>This is Hello!</h1>"


@app.route("/first")
def hello_first():
    return "<h1>Hello! First</h1>"


@app.route("/profile/<username>")
def get_profile(username):
    return "<h1>Profile: {}</h1>".format(username)


@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message: %d" % message_id


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
