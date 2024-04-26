#!/usr/bin/python3
"""
This script takes in a URL as an argument, sends a request to the URL,
and displays the value of the 'X-Request-Id' var found in response header.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    # Fetch the value of the 'X-Request-Id' header
    request_id = response.headers.get('X-Request-Id')
    print(request_id)
