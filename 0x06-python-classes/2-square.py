#!/usr/bin/python3
"""defines a class Square"""


class Square:
    """Represents a square."""

    
    def __init__(self, size=0):
        """initializes the square.

        Args:
            size (int): size of a side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
