#!/usr/bin/python3
"""Module for Square class."""

class Square:
    """Class that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square, defaults to 0.
            position (tuple): The position of the new square, defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
            return
        [print() for _ in range(self.__position[1])]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the string representation of the square."""
        if self.__size == 0:
            return ""
        square_str = "\n" * self.__position[1]
        for i in range(self.__size):
            square_str += " " * self.__position[0] + "#" * self.__size
            if i < self.__size - 1:
                square_str += "\n"
        return square_str

    def __lt__(self, other):
        """Define the less than comparison for Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the less than or equal to comparison for Square."""
        return self.area() <= other.area()
