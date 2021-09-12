from flask import Flask, Blueprint, request as req, render_template, redirect, url_for, session
from flask_login import current_user, login_user, logout_user
from blog_control.user_mgmt import User
from blog_control.session_mgmt import BlogSession
import datetime

blog_abtest = Blueprint('blog', __name__)


@blog_abtest.route("/set_email", methods=['GET', 'POST'])
def set_email():
    if req.method == 'GET':
        print("set_email", req.args.get("user_email"))
        return redirect(url_for('blog.test'))
    else:
        print('set_email', req.form['user_email'])
        user = User.create(req.form['user_email'], req.form['blog_id'])
        login_user(user, remember=True, duration=datetime.timedelta(days=365))

        return redirect(url_for('blog.test'))


@blog_abtest.route("/logout")
def logout():
    User.delete(current_user.id)
    logout_user()
    return redirect(url_for('blog.test'))


@blog_abtest.route("/test")
def test():
    if current_user.is_authenticated:
        webpage_name = BlogSession.get_blog_page(current_user.blog_id)
        BlogSession.save_session_info(
            session['client_id'], current_user.user_email, webpage_name
        )
        return render_template(webpage_name, user_email=current_user.user_email)
    else:
        webpage_name = BlogSession.get_blog_page()
        BlogSession.save_session_info(
            session['client_id'], 'anonymous', webpage_name
        )
        return render_template(webpage_name)
