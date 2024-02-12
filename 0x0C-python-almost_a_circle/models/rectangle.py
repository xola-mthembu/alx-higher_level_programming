#!/usr/bin/python3
"""
This module provides a Rectangle class that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle, inheriting from Base.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Gets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the Rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y coordinate of the Rectangle."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Returns the area value of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        """
        Prints the Rectangle instance with the character '#' to stdout,
        taking care of x and y.
        """
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Returns the string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle attributes with non-keyword
        arguments first, then keyword arguments.
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for attr, arg in zip(attrs, args):
                setattr(self, attr, arg)
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)
