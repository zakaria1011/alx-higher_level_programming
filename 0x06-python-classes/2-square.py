#!/usr/bin/python3

"""Defin a class squar """


class Square:
    """
    this classe define a squar.

    Attributes:
    __size(int) : size of the square

    Methodes:
    __init__(self, size = 0): initialise a square object with given size
    """
    def __init__(self, size=0):
        """
        initialise a new square object

        Args:
        size (int) : the size of the square

        Raise:
        TypeEroor: if size is not int
        ValueError: if size is negatif
        """
        if not isinstance(size, int):
            raise TypeError("size must be integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
