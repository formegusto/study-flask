from flask import Flask
from blog import blog

app = Flask(__name__)
app.register_blueprint(blog.blog_ab, url_prefix="/blog")


@app.route("/")
def main_page():
    return "<h1>Main Page</h1>"


if __name__ == "__main__":
    app.run(host="localhost", port=80, debug=True)
