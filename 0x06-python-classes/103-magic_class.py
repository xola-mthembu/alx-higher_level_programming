#!/usr/bin/python3
import math


class MagicClass:
    """A class that reps a circle with methods to cal its area and circ."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius.

        Args:
            radius (float or int): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        self.__check_type(radius)
        self.__radius = radius

    def __check_type(self, value):
        """Check if value is an int or float, raise TypeError if not."""
        if type(value) not in [int, float]:
            raise TypeError('radius must be a number')

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
