import json

def load_json(json_path):
    """
    Loads all the todos from the json file

    Args:
        json_path: path to json file

    Returns:
        dict: A dictionary containing the all todos, if file not exists the empty hirarchy will be created.
    """
    try:
        with open(json_path) as open_file:
            todolist = json.load(open_file)
    except FileNotFoundError:
        todolist = {"open":[],"done":[]}

    return todolist

def save_json(json_path, data):
    """
    Saves all the todos in the json file

    Args:
        json_path: path to json file
        dict: the data - all todos
    """
    with open(json_path, "w+", encoding="utf-8") as open_file:
        json.dump(data, open_file, indent=4)