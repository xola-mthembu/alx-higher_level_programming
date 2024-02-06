#!/usr/bin/python3
"""
Module 5-save_to_json_file
Contains a func that writes an Object to a txt file, using a JSON
representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a txt file, using a JSON rep."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
