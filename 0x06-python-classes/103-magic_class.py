#!/usr/bin/python3
import math

class MagicClass:
    """A class that represents a circle with methods to calculate its area and circumference."""

    def __init__(self, radius=0):
        """Initialize the MagicClass with a radius.

        Args:
            radius (float or int): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number.
        """
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

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
