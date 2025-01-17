#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display your ID.

Usage: ./10-my_github.py <username> <personal_access_token>
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    
    # Create session with Basic Authentication
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    auth = (username, token)
    
    # Send GET request
    r = requests.get(url, headers=headers, auth=auth)
    print(r.json().get('id'))
