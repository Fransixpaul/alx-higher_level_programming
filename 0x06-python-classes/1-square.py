#!/usr/bin/python3
"""This module defines a square class with a private attribute"""


class Square:
    """Defines a square"""

    def __init__(self, size):
        """Constructor.

        Args:
            size: length of a side of the square
        """
        self.__size = size
