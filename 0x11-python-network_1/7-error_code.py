#!/usr/bin/python3
"""
Script takes in a URL, sends a request, and displays the body of the res.
If the HTTP status code is 400 or above, it prints the error code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
