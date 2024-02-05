#!/usr/bin/python3
"""
Module 1-my_list - contains the MyList class that inherits from list.
"""


class MyList(list):
    """
    A subclass of list that includes a method for printing the list in
    sorted order.
    """
    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        print(sorted(self))
