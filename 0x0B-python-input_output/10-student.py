#!/usr/bin/python3

"""class student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """ initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ return dictionnary """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if attr in self.__dict__:
                result[attr] = self.__dict__[attr]
        return result
