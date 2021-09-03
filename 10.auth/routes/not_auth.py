from flask import Blueprint, request as req, redirect
from flask.templating import render_template
from flask_login import login_user, current_user, logout_user
from user import User
from common.messages import auth
import datetime

main_ab = Blueprint('', __name__)


@main_ab.route("/")
def main_page():
    msg = req.args.get("msg")
    msgIn = False
    if msg:
        if msg in auth.keys():
            msgIn = True
        else:
            msgIn = False
    if current_user.is_authenticated:
        return render_template("main.html", email=current_user.user_email, msg=auth[msg] if msgIn else False)
    else:
        return render_template("main.html", msg=auth[msg] if msgIn else False)


@main_ab.route("/login", methods=["GET"])
def login_page():
    if current_user.is_authenticated:
        return redirect("/?msg={}".format("already-auth"))
    msg = req.args.get("msg")
    msgIn = False
    if msg:
        if msg in auth.keys():
            msgIn = True
        else:
            msgIn = False
    return render_template("login.html", msg=auth[msg] if msgIn else False)


@main_ab.route("/join", methods=["GET"])
def join_page():
    if current_user.is_authenticated:
        return redirect("/?msg={}".format("need-logout"))
    msg = req.args.get("msg")
    msgIn = False
    if msg:
        if msg in auth.keys():
            msgIn = True
        else:
            msgIn = False
    return render_template("join.html", msg=auth[msg] if msgIn else False)


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
    if user == None:
        return redirect("/login?msg={}".format("not-exist-user"))
    login_user(user, remember=True, duration=datetime.timedelta(days=365))

    return redirect("/")


@main_ab.route("/join", methods=["POST"])
def join():
    data = req.form
    user_email = data['user-email']
    blog_id = data['blog-id']

    print("user_email:{}, blog_id: {}".format(user_email, blog_id))

    result, user = User.create(user_email, blog_id)
    if result:
        print("create user:{}".format(user))
        login_user(user, remember=True, duration=datetime.timedelta(days=365))
        return redirect("/")
    else:
        return redirect("/join?msg={}".format("exist-user"))
