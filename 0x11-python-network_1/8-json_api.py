#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.

Usage: ./8-json_api.py <letter>
"""
import requests
import sys


if __name__ == "__main__":
    # Set default value of q if no argument is provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Send POST request
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    
    try:
        # Try to parse JSON response
        json_response = r.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), 
                                 json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
