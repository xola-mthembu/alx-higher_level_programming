#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.
    Args:
    my_list (list): The initial list.
    search (any): The element to replace in the list.
    replace (any): The new element.
    Returns:
    list: New list with elements replaced.
    """
    return [replace if x == search else x for x in my_list]
