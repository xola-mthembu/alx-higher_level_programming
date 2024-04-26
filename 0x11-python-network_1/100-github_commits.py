#!/usr/bin/python3
"""
Script retrieves the last 10 commits of a specified repo and user
from GitHub's API and lists from most recent to oldest in the format:
<sha>: <author name>.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repo name> <owner>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits?per_page=10"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching commits: {response.status_code}")
        sys.exit(1)

    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
