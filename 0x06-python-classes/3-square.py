#!/usr/bin/python3

""" Define a classe square """


class Square:
    """
    This class defines a square.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square object
    """
    def __init__(self, size=0):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Return size of the square """
        return self.__size
