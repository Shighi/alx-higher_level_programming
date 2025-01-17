#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using urllib package.

This script demonstrates how to:
    - Make a GET request using urllib
    - Handle the response and read its content
    - Display response body information including type and content
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
