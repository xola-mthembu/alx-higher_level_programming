#!/usr/bin/python3
"""
Module 9-rect - Contains a class Rect that inherits from BaseGeometry.
Includes method implementations for area cal and string rep.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle, inheriting from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle with width and height validated by
        integer_validator from BaseGeometry.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the Rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return the Rectangle description.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
