#!/usr/bin/python3
"""
Module 10-student
Defines a Student class with a method to_json that includes filtering.
"""


class Student:
    """
    Represents a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        If attrs is a list of strings, retrieves only attributes
        contained in the list. Otherwise, retrieves all attributes.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                                           for attr in attrs):
            filtered_dict = {attr: getattr(self, attr) for attr in attrs
                             if hasattr(self, attr)}
            return filtered_dict
        return self.__dict__
