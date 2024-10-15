#!/usr/bin/python3
"""Module for appending a string to a text file."""


def append_write(filename="", text=""):
    """
    Append a string to the end of a text file (UTF8) and return the number of
    characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to "".
        text (str): The text to append to the file. Defaults to "".

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
