#!/usr/bin/python3

"""a function that save json to a file"""

import json


def save_to_json_file(my_obj, filename):
    """
    save a json to a file
    args:
    my_obj: object to make json represenation
    filename: file where to save json
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(my_obj, file)
