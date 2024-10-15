#!/usr/bin/python3
"""Module for converting a class to a JSON dictionary."""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure for JSON
    serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
