#!/usr/bin/python3
"""
Module 3-to_json_string
Contains a func that returns the JSON rep of an object (string).
"""
import json


def to_json_string(my_obj):
    """Return the JSON rep of an object (string)."""
    return json.dumps(my_obj)
