#!/usr/bin/python3
"""
Module 0-read_file
Contains func read_file that reads UTF-8 text file and prints it to stdout
"""


def read_file(filename=""):
    """Reads from 'filename' and prints its contents to stdout"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
