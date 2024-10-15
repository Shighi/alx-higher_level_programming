#!/usr/bin/python3
"""Module for inserting a line of text to a file after each specific string."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text to a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after the line containing the search string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
