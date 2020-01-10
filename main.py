import os
from pathlib import Path
from flask import Flask
from flask import render_template
from libs import data

app = Flask("jasmins todo")
app_main_path = Path(os.path.abspath("/".join(os.path.realpath(__file__).split("/")[:-1])))
data_path = Path(os.path.abspath(app_main_path / "data"))
data_storage_file = data_path / "todolist.json"

@app.route('/')
@app.route('/open')
def home():
    todolist = data.load_json(data_storage_file)
    return render_template('index.html', open_todos=todolist["open"])

@app.route('/done')
def done_todos():
    todolist = data.load_json(data_storage_file)
    return render_template('done_todos.html', done_todos=todolist["done"])

if __name__ == "__main__":
    app.run(debug=True, port=5000)