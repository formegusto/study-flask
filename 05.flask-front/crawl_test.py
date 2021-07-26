from flask import Flask
import requests as req

app = Flask(__name__)


@app.route("/")
def crawl_test():
    request = req.get("https://google.co.kr")

    return request.text


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
