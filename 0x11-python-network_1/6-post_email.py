#!/usr/bin/python3
"""
Script takes in a URL and an email, sends POST req to the URL with the
email as a parameter, and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the data for the POST request
    payload = {'email': email}

    # Send the POST request with the payload
    response = requests.post(url, data=payload)

    # Print the body of the response
    print(response.text)
