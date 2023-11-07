#!/usr/bin/python3
""" class rectangle inherite from BaseGeo """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class rectangle """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculate area """
        return self.__height * self.__width

    def __str__(self):
        """ Return the rectangle description as a string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
