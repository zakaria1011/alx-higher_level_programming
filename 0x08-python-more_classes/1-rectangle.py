#!/usr/bin/python3

""" class define rectangle """


class Rectangle:
    """ class triangle """
    
    def __init__(self, width=0, height=0):
        """
        initiate a rectangle

        Args:
        width (int): first arg
        height(int): seconde arg
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
