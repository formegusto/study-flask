from flask import Flask
import requests as req

app = Flask(__name__)


@app.errorhandler(404)
def err_404(error):
    return "<h1>Not Found Page</h1>"


@app.route("/google")
def google():
    res = req.get("https://google.co.kr")
    return res.text


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
