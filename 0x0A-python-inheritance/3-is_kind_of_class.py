#!/usr/bin/python3

""" check is object is from class or inherited class """


def is_kind_of_class(obj, a_class):
    """
    args:
    obj: object
    a_class: a class
    Return: true or false
    """
    return isinstance(obj, a_class)
