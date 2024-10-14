#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or inherited from, the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or inherited from a_class, False otherwise.
    """
    return isinstance(obj, a_class)
