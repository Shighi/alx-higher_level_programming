#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))  # Ensure that 'value' is printed as an integer
        return True
    except (ValueError, TypeError) as e:  # Handle only ValueError and TypeError
        print("Exception: {}".format(e), file=sys.stderr)  # Print the error to stderr
        return False
