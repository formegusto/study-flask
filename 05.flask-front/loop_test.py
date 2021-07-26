from flask import Flask, render_template

app = Flask(__name__)


@app.route("/gugu/<num>")
def gugudan(num):
    return render_template("loop.html", num=int(num))


@app.route("/list/<int:num>")
def list_text(num):
    return render_template("loop_2.html", values=["list {}".format(n) for n in range(num)])


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
