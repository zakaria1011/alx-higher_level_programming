#!/usr/bin/python3

""" function that read json from file and return an object"""

import json


def load_from_json_file(filename):
    """
    read from json from file and return an object

    args:
    filename : file
    """
    with open(filename, 'r') as file:
        return json.load(file)
