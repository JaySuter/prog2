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

def get_percent_open(count_open, count_total):
    if count_total > 0:
        return int(round(count_open / count_total * 100, 0))
    else:
        return "--"

def get_percent_done(count_done, count_total):
    if count_total > 0:
        return int(round(count_done / count_total * 100, 0))
    else:
        return "--"