#!/usr/bin/python3
"""
Script fetches the status from https://alx-intranet.hbtn.io/status
using the req package and formats the response body as specified.
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
