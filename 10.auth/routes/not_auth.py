from flask import Blueprint, request as req, redirect
from flask.templating import render_template
from flask_login import login_user, current_user, logout_user
from user import User
import datetime

main_ab = Blueprint('', __name__)


@main_ab.route("/")
def main_page():
    if current_user.is_authenticated:
        return render_template("main.html", email=current_user.user_email)
    return render_template("main.html")


@main_ab.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@main_ab.route("/join", methods=["GET"])
def join_page():
    return render_template("join.html")


@main_ab.route("/logout", methods=['GET'])
def logout():
    logout_user()
    return redirect("/")


@main_ab.route("/login", methods=['POST'])
def login():
    data = req.form
    user_email = data['user-email']

    print("user_email:{}".format(user_email))
    user = User.find(user_email)
    login_user(user, remember=True, duration=datetime.timedelta(days=365))

    return redirect("/")


@main_ab.route("/join", methods=["POST"])
def join():
    data = req.form
    user_email = data['user-email']
    blog_id = data['blog-id']

    print("user_email:{}, blog_id: {}".format(user_email, blog_id))

    user = User.create(user_email, blog_id)
    print("create user:{}".format(user))

    return redirect("/")
