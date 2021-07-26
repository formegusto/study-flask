from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cond/<int:num>")
def cond_test(num):
    return render_template("condition.html", num=num)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
