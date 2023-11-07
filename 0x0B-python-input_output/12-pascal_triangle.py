#!/usr/bin/python3

""" pascale triangle """


def fact(x):
    """ factorial """
    if x == 0:
        return 1
    return x * fact(x - 1)


def pascal_triangle(n):
    """ pascale triangle """
    result = []
    if n <= 0:
        return result
    for i in range(n):
        lists = []
        for k in range(i):
            elem_list = int(fact(i)/(fact(k) * fact(i - k)))
            lists.append(elem_list)
        result.append(lists)
    return result
