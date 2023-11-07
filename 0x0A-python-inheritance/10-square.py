#!/usr/bin/python3
""" class squar inherite from BaseGeo """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """ class Square """
    def __init__(self, size):
        """ initiation """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ calculate area """
        return self.__size
