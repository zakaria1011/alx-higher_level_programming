#!/usr/bin/python3

""" function that append text at the end of """


def append_write(filename="", text=""):
    """
    append text at the end of a file
    args:
    filename: the file
    text: text to append
    """
    with open(filename, 'a') as file:
        file.write(text)
        num_of_carac = len(text)
        return num_of_carac
