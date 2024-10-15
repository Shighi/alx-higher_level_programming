#!/usr/bin/python3
"""Module defining a class BaseGeometry with a method raising an exception."""


class BaseGeometry:
    """A class for geometric shapes."""

    def area(self):
        """Raises an Exception indicating that area is not implemented."""
        raise Exception("area() is not implemented")
