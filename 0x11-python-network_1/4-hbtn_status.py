#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status using requests package.

This script demonstrates how to:
    - Make a GET request using requests
    - Access response content
    - Display response body information
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
