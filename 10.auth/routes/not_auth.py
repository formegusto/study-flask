from flask import Blueprint, request as req
import flask
from flask.templating import render_template
from user import User

main_ab = Blueprint('', __name__)


@main_ab.route("/")
def main_page():
    return render_template("main.html")


@main_ab.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@main_ab.route("/join", methods=["GET"])
def join_page():
    return render_template("join.html")


@main_ab.route("/join", methods=["POST"])
def join():
    data = req.form
    user_email = data['user-email']
    blog_id = data['blog-id']

    print("user_email:{}, blog_id: {}".format(user_email, blog_id))

    user = User.create(user_email, blog_id)
    print("create user:{}".format(user))

    return flask.redirect("/")
