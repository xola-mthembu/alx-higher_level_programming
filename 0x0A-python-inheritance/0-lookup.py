#!/usr/bin/python3
"""
Module 0-lookup
Contains method lookup that returns a list of available attributes and methods
of an object.
"""


def lookup(obj):
    """
    Returns a list object containing the list of available attributes and
    methods of an object.
        Args:
        obj: The object to lookup.

    Returns:
        A list of attributes and methods of the object.
    """
    return dir(obj)
