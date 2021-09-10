from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app,
          version='0.1',
          title="formegusto's flask study",
          description="Hello :)",
          terms_url="/",
          contact="formegusto@gmail.com",
          license="MIT"
          )
namespace = Namespace('hello')


@namespace.route("/")
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world!"}, 201, {"hi": "hello"}


api.add_namespace(namespace, "/hello")


@api.route("/main")
class Main(Resource):
    def get(self):
        return "This is Main!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=80)
