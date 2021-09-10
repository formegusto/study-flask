from flask import Flask
from flask_restx import Api
from todos_app import todos_space

app = Flask(__name__)
api = Api(app,
          version='0.1',
          title="formegusto's flask study",
          description="Hello :)",
          terms_url="/",
          contact="formegusto@gmail.com",
          license="MIT"
          )

api.add_namespace(todos_space, "/todos")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
