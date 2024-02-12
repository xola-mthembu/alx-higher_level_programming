#!/usr/bin/python3
"""
This module provides a Base class.
"""
import json


class Base:
    """A base class for all models in the project."""
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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, 'w') as f:
            f.write(json_string)

# Include other previously defined methods...
