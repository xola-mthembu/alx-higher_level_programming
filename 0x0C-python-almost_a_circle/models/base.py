#!/usr/bin/python3
"""
Module provides a Base class for all other classes in the project.
This serves as the foundation class, with common functionality.
"""
import json


class Base:
    _nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    # Continue with the rest of the Base class implementation...
