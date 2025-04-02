def list_operations():
    """Performs insert, delete, and find operations on a list."""
    my_list = [1, 2, 3, 4, 5]
    my_list.append(6)  # Insert
    my_list.remove(3)  # Delete
    found = 4 in my_list  # Find
    return my_list, found
