#!/usr/bin/python3
"""Module providing a function to check if an object is an instance of a class
or inherits from it."""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or a class that inherited
    from a_class."""
    return isinstance(obj, a_class)
