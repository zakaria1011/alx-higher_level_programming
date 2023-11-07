#!/usr/bin/python3

"""function that open a file """


def read_file(filename=""):
    """
    open a file
    args:
    file
    """
    with open(filename, 'r') as file:
        for line in file:
            print(line, end='')
