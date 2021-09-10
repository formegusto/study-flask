from flask.globals import request as req
import jwt
import bcrypt
from flask import request as req
from flask_restx import Resource, Api, Namespace, fields

Auth = Namespace("Auth API", description="사용자 인증을 위한 API")
secret = "formegusto"
users = {}

user_fields = Auth.model('User', {
    'name': fields.String(description="a User Name", required=True, example="formegusto")
})

user_fields_auth = Auth.inherit("User Auth", user_fields, {
    'password': fields.String(description="Password", required=True, example="password")
})

jwt_fields = Auth.model("JWT", {
    "Authorization": fields.String(description="Authorization which you must includ in header", required=True, example="eyJ0e~~~")
})


@Auth.route('/register')
class AuthRegister(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.response(200, "Success", jwt_fields)
    @Auth.doc(responses={500: "Register Failed"})
    def post(self):
        name = req.json['name']
        password = req.json['password']
        if name in users:
            return {
                "message": "Register Failed"
            }, 500
        else:
            users[name] = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt())
            return {
                'Authorization': jwt.encode({
                    "name": name,
                }, secret,
                    algorithm="HS256")
            }, 200


@Auth.route("/login")
class AuthLogin(Resource):
    @Auth.expect(user_fields_auth)
    @Auth.response(200, "Success", jwt_fields)
    @Auth.doc(responses={404: 'User Not Found'})
    @Auth.doc(responses={500: 'Auth Failed'})
    def post(self):
        name = req.json['name']
        password = req.json['password']

        if name not in users:
            return {
                "message": "User Not Found"
            }, 404
        elif not bcrypt.checkpw(password.encode('utf-8'), users[name]):
            return {
                "message": "Auth Failed"
            }, 500
        else:
            return {
                'Authorization': jwt.encode({
                    "name": name,
                }, secret,
                    algorithm="HS256")
            }, 200


@Auth.route("/get")
class AuthGet(Resource):
    @Auth.response(200, "Success", user_fields)
    @Auth.doc(responses={404: "Login Failed"})
    def get(self):
        header = req.headers.get("Authorization")
        if header == None:
            return {"message": "Please Login"}, 404
        try:
            data = jwt.decode(header, secret, algorithms="HS256")
        except:
            return {"message": "Bad Token"}, 400

        return data, 200
