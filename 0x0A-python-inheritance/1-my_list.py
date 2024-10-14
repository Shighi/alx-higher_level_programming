#!/usr/bin/python3
class MyList(list):
    """A class that inherits from list and provides a sorted print method"""

    def print_sorted(self):
        """Prints the list, but sorted in ascending order"""
        print(sorted(self))
