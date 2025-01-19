#!/usr/bin/python3
"""
Script that lists 10 most recent commits of a repository by a specified user.

Usage: ./100-github_commits.py <repository_name> <repository_owner>
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    
    # Format URL for GitHub API
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    
    # Send GET request with parameters
    r = requests.get(url, params={'per_page': 10})
    
    # Process and display commits
    for commit in r.json():
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
