#!/usr/bin/python3
"""
Module 100-my_int - Contains class MyInt that inherits from int and inverts
the == and != operators.
"""


class MyInt(int):
    """
    MyInt is a rebel class that inverts the == and != comparison operators.
    """
    def __eq__(self, other):
        """
        Invert the == operator.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Invert the != operator.
        """
        return super().__eq__(other)
