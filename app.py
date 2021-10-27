from flask import Flask, request
from todo import Todo

app = Flask(__name__)

@app.route('/todo/<int:recordID>', methods=['GET'])
def get_todo(recordID):
    if request.method == "GET":
        todo = Todo(recordID)
        return (todo.getTodo())
    return {"status": 200, "content": {} }

if __name__ == "__main__":
    app.run(port=5002, debug=True)
