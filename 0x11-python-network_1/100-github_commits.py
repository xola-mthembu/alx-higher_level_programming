#!/usr/bin/python3
"""
Script retrieves the last 10 commits from a specified repo and usr
from GitHub's API and lists them from the most recent to oldest.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./100-github_commits.py <repo name> <owner>")
        sys.exit(1)

    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch commits: {response.status_code}")
        sys.exit(1)

    commits = response.json()
    for commit in commits[:10]:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")
