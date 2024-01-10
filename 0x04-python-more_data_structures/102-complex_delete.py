#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.
    Args:
    a_dictionary (dict): The dictionary to modify.
    value (any): The value whose keys should be deleted.
    """
    keys_to_delete = [key for key, val in a_dictionary.items() if val == value]
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
