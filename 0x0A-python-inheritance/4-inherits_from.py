#!/usr/bin/python3

""" check if an object inherite directly or inderectly """


def inherits_from(obj, a_class):
    """
    arg:
    obj: object
    a_class : a classe
    """
    return issubclass(obj, a_class)
