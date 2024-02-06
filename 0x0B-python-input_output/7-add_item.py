#!/usr/bin/python3
"""
This script adds all args to a Python list, and then save them to a file.
"""
import sys
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Creates an object from a 'JSON file'."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []


if __name__ == "__main__":
    filename = "add_item.json"
    items = load_from_json_file(filename)
    items.extend(sys.argv[1:])
    save_to_json_file(items, filename)
