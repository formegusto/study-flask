from flask import Flask
from flask_restx import Api
from auth import Auth

app = Flask(__name__)
api = Api(app)

api.add_namespace(Auth, "/auth")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
