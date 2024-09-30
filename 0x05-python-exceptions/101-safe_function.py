#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        result = fct(*args)  # Attempt to call the function
        return result  # Return the result if successful
    except Exception as e:  # Catch any exception
        print("Exception: {}".format(e), file=sys.stderr)  # Print the error to stderr
        return None  # Return None if there is an exception
