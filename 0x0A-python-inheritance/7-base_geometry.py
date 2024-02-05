#!/usr/bin/python3
"""
Module 7-base_geometry - Enhances the BaseGeometry class with an integer
validator method.
"""


class BaseGeometry:
    """
    A class BaseGeometry with methods for area cal and integer validation.
    """
    def area(self):
        """
        Raises an Exc with the message that the method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that the value is a positive integer.
        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
