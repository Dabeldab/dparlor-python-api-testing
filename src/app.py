from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False, "id": 1},
    { "label": "My second task", "done": False, "id": 2},
]
    
@app.route('/todos', methods=['GET'])
def hello_world():    
    return jsonify(todos), 200
    
@app.route('/', methods=['GET'])
def hello():
    return "<h1>Hello World</>"


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    return jsonify('Todo added', request_body)

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    print("This is the position to delete:", id)
    return jsonify(id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port =3245, debug=True)
    