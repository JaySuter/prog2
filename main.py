import os
from pathlib import Path
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from libs import data

app = Flask("jasmins todo")
app_main_path = Path(os.path.abspath("/".join(os.path.realpath(__file__).split("/")[:-1])))
data_path = Path(os.path.abspath(app_main_path / "data"))
data_storage_file = data_path / "todolist.json"

@app.route('/', methods=['GET', 'POST'])
@app.route('/open', methods=['GET', 'POST'])
def home():
    error_message = None
    todolist = data.load_json(data_storage_file)

    if request.method == 'POST':
        new_todo = request.form['todo_text']

        if new_todo in todolist['open']:
            error_message = "ToDo already exists!"
        else:
            todolist['open'].append(new_todo)
            data.save_json(data_storage_file, todolist)

    return render_template('index.html', open_todos=todolist["open"], error=error_message)
    


@app.route('/mark_as_done/<todo_as_done>')
def mark_as_done(todo_as_done=None):
    todolist = data.load_json(data_storage_file)

    if todo_as_done:
        if todo_as_done in todolist['open']:
            todolist['open'].remove(todo_as_done)
            todolist['done'].append(todo_as_done)
            data.save_json(data_storage_file, todolist)
    
    return redirect(url_for('home'))


@app.route('/done', methods=['GET', 'POST'])
def done_todos():
    todolist = data.load_json(data_storage_file)

    return render_template('done_todos.html', done_todos=todolist["done"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)