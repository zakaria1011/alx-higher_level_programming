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
        """
        self.__size = size

    def size(self):
        """ retrieve the size of square)"""
        return self.__size

    def size(self, value):
        """ control the type of the velue """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Return area of the square """
        return self.__size ** 2
