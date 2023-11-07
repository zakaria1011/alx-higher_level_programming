#!/usr/bin/python3

""" function that write in file  """


def write_file(filename="", text=""):
    """
    write in a file
    return number of caractere writen
    args:
    filename : file
    text: text to write
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        num_of_carac = file.tell()
    return num_of_carac
