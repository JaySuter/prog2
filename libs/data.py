import json

def load_json(json_path):
    try:
        with open(json_path) as open_file:
            todolist = json.load(open_file)
    except FileNotFoundError:
        todolist = {"open":[],"done":[]}

    return todolist

def save_json(json_path, data):
    with open(json_path, "w+", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)