#!/usr/bin/python3
"""Module defining a class MyList that inherits from list."""


class MyList(list):
    """A class that inherits from list and adds a method to print the list
    in sorted order."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
