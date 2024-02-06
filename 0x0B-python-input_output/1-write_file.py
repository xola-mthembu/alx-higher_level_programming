#!/usr/bin/python3
"""
Module 1-write_file
Contains a func that writes a string to a txt file (UTF8) and
returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Writes 'txt' to 'filename' and returns number of chars written."""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
