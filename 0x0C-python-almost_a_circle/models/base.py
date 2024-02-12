#!/usr/bin/python3
"""
This module provides the Base class as a foundation for all other classes
in the project, ensuring compliance with PEP 8 styling and functionality for
JSON serialization/deserialization, file handling, and visual representation
using Turtle graphics.
"""
import json
import csv
import os
import turtle


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
        with open(filename, 'w') as f:
            list_dicts = [obj.to_dictionary() for obj in list_objs] if list_objs else []
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV format and saves it to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['id', 'width', 'height', 'x', 'y'] \
                if cls.__name__ == "Rectangle" else ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes from CSV format and returns a list of instances."""
        filename = f"{cls.__name__}.csv"
        if not os.path.isfile(filename):
            return []
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            return [cls.create(**{k: int(v) for k, v in row.items()})
                    for row in reader]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using Turtle graphics."""
        turtle.speed(1)
        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            for _ in range(2):
                turtle.forward(rect.width)
                turtle.right(90)
                turtle.forward(rect.height)
                turtle.right(90)
        for sq in list_squares:
            turtle.penup()
            turtle.goto(sq.x, sq.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(sq.size)
                turtle.right(90)
        turtle.done()
