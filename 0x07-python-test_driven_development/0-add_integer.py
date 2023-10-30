#!/usr/bin/python3

""" function that add two integer or float """


def add_integer(a, b=98):
    """
    this function take two integer and return the sum

    args:
    a (int or float): first variable
    b (int or float): seconde variable

    returns:
    cast to int and return
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
