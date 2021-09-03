from flask import Flask
from flask_login import LoginManager
from routes.not_auth import main_ab
from user import User
import os

app = Flask(__name__, template_folder="view", static_url_path="/static")
app.register_blueprint(main_ab, url_prefix="/")

# 1. Config Secret Key
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.secret_key = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'


@login_manager.user_loader
def load_user(user_id):
    print("userid:", user_id)
    return User.get(user_id)


if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=True)
