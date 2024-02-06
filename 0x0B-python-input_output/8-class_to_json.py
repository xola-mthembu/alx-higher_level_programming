#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a func that returns the dictionary description with simple data
structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an obj."""
    return obj.__dict__
