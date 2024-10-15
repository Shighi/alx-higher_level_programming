#!/usr/bin/python3
"""Module for MyInt class that inherits from int."""


class MyInt(int):
    """MyInt class that inherits from int and inverts comparison operators."""

    def __eq__(self, other):
        """Invert the equality operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert the inequality operator."""
        return super().__eq__(other)
