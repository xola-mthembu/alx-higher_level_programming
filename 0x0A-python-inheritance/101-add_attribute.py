#!/usr/bin/python3
"""
Module 101-add_attribute - Adds a new attribute to an object if possible.
"""


def add_attribute(obj, attr, value):
    """
    Adds a new attr to an object if it's possible.

    Args:
        obj: The object to add an attribute to.
        attr (str): The name of the attribute to add.
        value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
