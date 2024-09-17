#!/usr/bin/python3
# Import the add function from add_0.py
from add_0 import add

if __name__ == "__main__":
    # Assign values to a and b
    a = 1
    b = 2

    # Print the result using string formatting
    print("{} + {} = {}".format(a, b, add(a, b)))
