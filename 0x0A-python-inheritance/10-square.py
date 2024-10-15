#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square with a size."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the Square."""
        return f"[Rectangle] {self.__size}/{self.__size}"
