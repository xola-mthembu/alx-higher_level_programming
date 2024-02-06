#!/usr/bin/python3
"""
Module 100-append_after
Contains a function that inserts a line of text to a file, after each line
containing a specific string.
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts line of txt to a file, after line containing a specific str."""
    with open(filename, "r") as f:
        lines = f.readlines()

    with open(filename, "w") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
