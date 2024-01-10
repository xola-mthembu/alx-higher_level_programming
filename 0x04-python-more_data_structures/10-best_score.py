#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.
    Args:
    a_dictionary (dict): The dictionary to search.
    Returns:
    Any: The key with the highest value, or None if no scores are found.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
