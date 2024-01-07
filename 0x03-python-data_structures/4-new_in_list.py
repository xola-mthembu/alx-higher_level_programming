#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a copy of the list at a specific position.
    """
    new_list = my_list[:]
    if 0 <= idx < len(new_list):
        new_list[idx] = element
    return new_list
