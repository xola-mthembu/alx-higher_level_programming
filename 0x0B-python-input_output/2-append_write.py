#!/usr/bin/python3
"""
Module 2-append_write
Contains a func that appends a string at the end of a txt file (UTF8)
and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """Appends 'txt' to 'filename' and returns number of chars added."""
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
