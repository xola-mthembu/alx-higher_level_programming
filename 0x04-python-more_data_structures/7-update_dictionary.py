#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    Args:
    a_dictionary (dict): The dictionary to update.
    key (str): The key to add or update in the dictionary.
    value (any): The value to be associated with the key.
    """
    a_dictionary[key] = value
    return a_dictionary
