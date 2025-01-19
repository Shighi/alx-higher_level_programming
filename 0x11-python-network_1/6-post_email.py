#!/usr/bin/python3
"""
Script that takes in a URL and an email address, sends a POST request
to the URL with the email as a parameter, and displays the response body.

Usage: ./6-post_email.py <URL> <email>
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Send POST request with email parameter
    r = requests.post(url, data={'email': email})
    print(r.text)
