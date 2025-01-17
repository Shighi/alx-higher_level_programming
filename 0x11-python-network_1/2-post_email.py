#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.

Usage: ./2-post_email.py <URL> <email>
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data for POST request
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    
    # Create and send the request
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))
