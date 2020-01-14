import os
from pathlib import Path
from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from libs import data
from libs import statistics

app = Flask("jasmins todo")
app_main_path = Path(os.path.abspath("/".join(os.path.realpath(__file__).split("/")[:-1])))
data_path = Path(os.path.abspath(app_main_path / "data"))
data_storage_file = data_path / "todolist.json"

@app.route('/', methods=['GET', 'POST'])
@app.route('/open', methods=['GET', 'POST'])
def home():
    """
    Show the home page when the url/route is '/' or '/home'.
    On the home page all todos will be shown which are open.

    Returns:
        template: The template index.html will be rendered with all open todos and the statistics.
    """
    error_message = None
    todolist = data.load_json(data_storage_file)

    if request.method == 'POST':
        new_todo = request.form['todo_text']

        if new_todo in todolist['open']:
            error_message = "ToDo already exists!"
        else:
            todolist['open'].append(new_todo)
            data.save_json(data_storage_file, todolist)

    count_open = statistics.get_count_open(todolist)
    count_done = statistics.get_count_done(todolist)
    count_total = int(count_open+count_done)
    percent_open = statistics.get_percent_open(count_open, count_total)
    percent_done = statistics.get_percent_done(count_done, count_total)

    return render_template('index.html', open_todos=todolist["open"], error=error_message, count_total=count_total, count_open=count_open, count_done=count_done, percent_open=percent_open, percent_done=percent_done)
    


@app.route('/done')
def done_todos():
    """
    Show the done page when the url/route is '/done'.
    On the done page all todos will be shown which are done.

    Returns:
        template: The template done_todos.html will be rendered with all done todos and the statistics.
    """
    todolist = data.load_json(data_storage_file)

    count_open = statistics.get_count_open(todolist)
    count_done = statistics.get_count_done(todolist)
    count_total = int(count_open+count_done)
    percent_open = statistics.get_percent_open(count_open, count_total)
    percent_done = statistics.get_percent_done(count_done, count_total)

    return render_template('done_todos.html', done_todos=todolist["done"], count_total=count_total, count_open=count_open, count_done=count_done, percent_open=percent_open, percent_done=percent_done)



@app.route('/mark_as_done/<todo_as_done>')
def mark_as_done(todo_as_done=None):
    """
    Marks an open todo item as done.

    Args:
        todo_as_done: name of the open todo item

    Returns:
        redirect: The user will be redirected to the home page.
    """
    todolist = data.load_json(data_storage_file)

    if todo_as_done:
        if todo_as_done in todolist['open']:
            todolist['open'].remove(todo_as_done)
            todolist['done'].append(todo_as_done)
            data.save_json(data_storage_file, todolist)
    
    return redirect(url_for('home'))



@app.route('/mark_as_open/<todo_as_open>')
def mark_as_open(todo_as_open=None):
    """
    Marks a done todo item as open.

    Args:
        todo_as_open: name of the done todo item

    Returns:
        redirect: The user will be redirected to the done_todos page.
    """
    todolist = data.load_json(data_storage_file)

    if todo_as_open:
        if todo_as_open in todolist['done']:
            todolist['done'].remove(todo_as_open)
            todolist['open'].append(todo_as_open)
            data.save_json(data_storage_file, todolist)
    
    return redirect(url_for('done_todos'))


@app.route('/delete/<todo_as_open>')
def delete_item(todo_as_open=None):
    """
    Marks a done todo item as open.

    Args:
        todo_as_open: name of the done todo item

    Returns:
        redirect: The user will be redirected to the done_todos page.
    """
    todolist = data.load_json(data_storage_file)

    if todo_as_open:
        if todo_as_open in todolist['done']:
            todolist['done'].remove(todo_as_open)
        elif todo_as_open in todolist['open']:
            todolist['open'].remove(todo_as_open)
        data.save_json(data_storage_file, todolist)
    
    return redirect(url_for('done_todos'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)

