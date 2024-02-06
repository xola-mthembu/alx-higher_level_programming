#!/usr/bin/python3
"""
Module 4-from_json_string
Contains a func that returns an object rep by a JSON string.
"""
import json


def from_json_string(my_str):
    """Return an object rep by a JSON string."""
    return json.loads(my_str)
