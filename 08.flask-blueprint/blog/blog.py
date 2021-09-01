from flask import Blueprint

blog_ab = Blueprint('blog', __name__)


@blog_ab.route("/")
def blog_main_page():
    return "<h1>Blog Main Page</h1>"
