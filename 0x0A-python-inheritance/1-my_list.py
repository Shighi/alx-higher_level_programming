#!/usr/bin/python3
class MyList(list):
    """
    A class that inherits from list and implements a print_sorted method.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
