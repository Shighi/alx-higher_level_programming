#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.
        """
        return self.__size ** 2
