#!/usr/bin/python3

""" function that print squire of # """


def print_square(size):
    """
    take size and print square

    args:
    size (int): size of the squire
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
