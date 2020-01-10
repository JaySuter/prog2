def get_count_open(todolist):
    """
    Get the count of all open todo items

    Args:
        dict: the data - all todos

    Returns:
        int: the count of all open todo items as int
    """
    return int(len(todolist["open"]))

def get_count_done(todolist):
    """
    Get the count of all done todo items

    Args:
        dict: the data - all todos

    Returns:
        int: the count of all done todo items as int
    """
    return int(len(todolist["done"]))