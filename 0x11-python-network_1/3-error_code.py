#!/usr/bin/python3
"""
This script takes in a URL, sends a req to the URL, and displays the body of
the res decoded in utf-8. If an HTTP error occurs, the error code is printed.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Print the HTTP error code if an error occurs
        print(f"Error code: {e.code}")
