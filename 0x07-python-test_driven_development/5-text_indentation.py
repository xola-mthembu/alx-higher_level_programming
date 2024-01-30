#!/usr/bin/python3
"""
This module provides a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each ., ? and :
    Args:
        text: The text to be printed
    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i], end="")
            if i < len(text) - 1:
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end="")
        i += 1
