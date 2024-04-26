#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST req to the URL with the
email as a parameter, and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')  # data should be bytes

    # Create a request object with the data
    req = urllib.request.Request(url, data)

    # Perform the POST request and fetch the response
    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
