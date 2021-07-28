from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/test", methods=['GET', 'POST', 'PUT', 'DELETE'])
def get_test():
    method_type = request.method
    if method_type == "GET":
        print("GET")
        user = request.args.get("email")
        print(user)
    elif method_type == "POST":
        print("POST")
        data = request.get_json()
        print(data['email'])
    elif method_type == "PUT":
        print("PUT")
        data = request.get_json()
        print("data", data)
        user = request.args.get("email")
        print(user)
    elif method_type == "DELETE":
        print("DELETE")
        user = request.args.get("email")
        print(user)

    return make_response(jsonify(success=True), 200)


if __name__ == "__main__":
    app.run(host="localhost", port="8080")
