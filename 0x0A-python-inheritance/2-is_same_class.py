#!/usr/bin/python3

""" a function that check is an object is an instrance of a class """


def is_same_class(obj, a_class):
    """
    args:
    obj: object
    a_class: class

    Return : True or fals
    """
    return isinstance(obj, a_class)
