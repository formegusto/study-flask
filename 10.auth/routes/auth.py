from flask import Blueprint, redirect
from flask.templating import render_template
from flask_login import current_user

board_ab = Blueprint("blog", __name__)


@board_ab.route("/")
def board_page():
    if not current_user.is_authenticated:
        return redirect("/?msg={}".format('need-auth'))
    return render_template("board.html")
