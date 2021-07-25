from flask import Flask, jsonify, request, render_template

app = Flask(__name__, static_url_path="/static")


@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if (username == "formegusto") & (password == "1234"):
        rtn_data = {"auth": "success"}
    else:
        rtn_data = {"auth": "failure"}

    return jsonify(rtn_data)


@app.route("/")
def login_page():
    return render_template("bootstrap_login.html")


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
