from flask import request as req
from flask_restx import Resource, Namespace, fields


class Todos():
    def __init__(self, id, todo):
        self.id = id
        self.todo = todo

    def get_dict(self):
        return {
            "id": self.id,
            "todo": self.todo
        }


todos = list()
count = 0

todos_space = Namespace(
    name="Todos",
    description="Todo 리스트를 작성하기 위해 사용하는 API"
)
todo_fields = todos_space.model('Todos', {
    'data': fields.String(description='a Todo', required=True, example="what to do")
})
todo_fields_with_id = todos_space.model('Todo With ID', {
    'id': fields.Integer(description="a Todo ID"),
    "todo": fields.String(description="a Todo Content")
})


@todos_space.route("")
class SimpleTodosApi(Resource):
    def get(self):
        '''TodoList를 가져옵니다.'''
        return {
            "todos":
            [todo.get_dict() for todo in todos]
        }

    @todos_space.expect(todo_fields)
    @todos_space.response(201, 'Success', todo_fields_with_id)
    def post(self):
        '''TodoList에 새로운 할 일을 등록합니다.'''
        global todos
        global count

        idx = count
        count += 1

        todo = Todos(idx, req.json.get("data"))
        todos.append(todo)

        return todo.get_dict(), 201


@todos_space.route("/<int:todo_id>")
@todos_space.doc(params={'todo_id': 'An ID'})
class SimpleTodosApiWithId(Resource):
    def get(self, todo_id):
        '''특정 todo의 내용만을 가져옵니다.'''
        global todos
        todo = next((todo for todo in todos if todo.id == todo_id), None)

        return {
            "todo": None if todo == None else todo.get_dict()
        }

    def put(self, todo_id):
        '''Todolist에 todo_id와 일치하는 id를 가진 todo를 수정합니다.'''
        global todos
        todo = next((todo for todo in todos if todo.id == todo_id), None)

        if todo != None:
            todo.todo = req.json.get("data")

        return {
            "todo": None if todo == None else todo.get_dict()
        }

    @todos_space.doc(responses={202: 'Success'})
    @todos_space.doc(responses={400: "똑바로 보내주시죠?"})
    def delete(self, todo_id):
        '''Todolist에 특정 할 일을 삭제합니다.'''
        global todos
        todos = list(filter(lambda todo: todo.id != todo_id, todos))

        return {
            "success": True
        }, 202
