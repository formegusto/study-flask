from flask import Flask

app = Flask(__name__)


@app.before_first_request
def before_first_request():
    print("플라스크 실행 후, 첫 요청에만 동작")


@app.before_request
def before_request():
    print("웹 브라우저 요청이 들어가기 전에 실행")


@app.route("/")
def page():
    print("본문 페이지")
    return "<h1>하이</h1>"


@app.after_request
def after_request(res):
    print("브리우저에 응답하기 전에 실행")
    return res


if __name__ == "__main__":
    app.run(host="localhost", port=80, debug=True)
