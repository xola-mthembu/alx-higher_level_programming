#!/usr/bin/python3
"""
Script takes a letter as a command-line arg, sends a POST req with
the letter as a parameter, and processes the JSON response.
"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    response = requests.post(url, data={'q': q})
    try:
        result = response.json()
        if result:
            print(f"[{result['id']}] {result['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
