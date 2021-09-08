from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {"hello": "world!"}


@api.route('/hello/<string:name>')
class HelloWorldWithName(Resource):
    def get(self, name):
        return {"message": "hello! {}".format(name)}, 201, {"hello": "itsheader!"}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
