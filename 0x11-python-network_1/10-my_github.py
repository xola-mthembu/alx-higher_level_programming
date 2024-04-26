#!/usr/bin/python3
"""
Script takes GitHub cred (username and a personal access token)
and uses the GitHub API to display the user's ID.
It securely accesses the personal access token from an env var.
"""
import requests
import sys
import os  # Import os to access environment variables


if __name__ == "__main__":
    username = 'xola-mthembu'
    token = os.getenv('GITHUB_TOKEN')

    url = f'https://api.github.com/users/{username}'
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.json()['id'])
    else:
        print(f"Failed to retrieve usr data: {response.status_code}")
