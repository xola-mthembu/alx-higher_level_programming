#!/usr/bin/python3
"""
This module provides a Base class.
Base class is the foundation of all other classes in this project.
"""
import json
import os


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
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        list_dicts = ([obj.to_dictionary() for obj in list_objs]
                      if list_objs else [])
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(list_dicts))

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file."""
        filename = f"{cls.__name__}.json"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r') as f:
            list_dicts = cls.from_json_string(f.read())
        return [cls.create(**dct) for dct in list_dicts]
