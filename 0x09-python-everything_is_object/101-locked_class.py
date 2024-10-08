#!/usr/bin/python3
"""Define a locked class."""


class LockedClass:
    """
    Prevent user from creating new instance attributes
    except if the attribute is called 'first_name'.
    """
    __slots__ = ['first_name']
