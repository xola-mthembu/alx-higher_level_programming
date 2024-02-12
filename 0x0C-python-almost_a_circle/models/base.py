#!/usr/bin/python3
"""
This module provides a Base class.
"""
import json


class Base:
    """A base class for all models in the project."""
    _nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

# Continue with other previously defined methods...
