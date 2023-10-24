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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square object.

        Args:
            size (int): The size of the square.
            position (tuple): the position
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ retrieve the size of square)"""
        return self.__size

    @size.setter
    def size(self, value):
        """ control the type of the velue """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrieve the position """
        return self.__position

    @position.setter
    def position(self, value):
        """control the type of the position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(x, int) for x in value) or
                not all(x >= 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return area of the square """
        return self.__size ** 2

    def my_print(self):
        """ Print the square with #"""
        if self.__size == 0:
            print()
            return
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
            print()
