#!/usr/bin/python3
""" class squar inherite from BaseGeo """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square """
    def __init__(self, size):
        """ initiation """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculate area """
        return self.__size
