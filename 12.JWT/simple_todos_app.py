from flask import Flask, request as req
from flask_restx import Api, Resource


class Todos():
    def __init__(self, id, todo):
        self.id = id
        self.todo = todo

    def get_dict(self):
        return {
            "id": self.id,
            "todo": self.todo
        }


app = Flask(__name__)
api = Api(app)
todos = list()
count = 0


@api.route("/todos")
class SimpleTodosApi(Resource):
    def get(self):
        return {
            "todos":
            [todo.get_dict() for todo in todos]
        }

    def post(self):
        global todos
        global count

        idx = count
        count += 1

        todo = Todos(idx, req.json.get("data"))
        todos.append(todo)

        return todo.get_dict(), 201


@api.route("/todos/<int:todo_id>")
class SimpleTodosApiWithId(Resource):
    def get(self, todo_id):
        global todos
        todo = next((todo for todo in todos if todo.id == todo_id), None)

        return {
            "todo": None if todo == None else todo.get_dict()
        }

    def put(self, todo_id):
        global todos
        todo = next((todo for todo in todos if todo.id == todo_id), None)

        if todo != None:
            todo.todo = req.json.get("data")

        return {
            "todo": None if todo == None else todo.get_dict()
        }

    def delete(self, todo_id):
        global todos
        todos = list(filter(lambda todo: todo.id != todo_id, todos))

        return {
            "success": True
        }


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
