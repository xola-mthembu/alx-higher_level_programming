#!/usr/bin/python3
"""
Module 11-student
Def Student class with methods for JSON serialization and deserialization.
"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Filters attributes based on attrs, a list of strings.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs
                    if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a json dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
