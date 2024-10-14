#!/usr/bin/python3
class BaseGeometry:
    """
    A class with area() and integer_validator() methods.
    """
    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer: raise a TypeError exception
        - If value is less or equal to 0: raise a ValueError exception
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
