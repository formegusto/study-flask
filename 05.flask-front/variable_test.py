from flask import Flask, render_template

app = Flask(__name__)


@app.route("/hello/<user>")
def hello_user(user):
    return render_template("variable.html", name=user)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
