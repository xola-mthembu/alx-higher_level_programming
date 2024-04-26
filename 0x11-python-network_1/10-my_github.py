#!/usr/bin/python3
"""
Script uses GitHub API to display GitHub usr ID based on the usrname
and a personal access token provided as command-line arguments.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./10-my_github.py <username> <personal_access_token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/users/{username}"

    # Make an authenticated request to the GitHub API
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("Failed to retrieve user data")
        sys.exit(1)
