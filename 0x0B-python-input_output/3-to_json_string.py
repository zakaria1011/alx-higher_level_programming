#!/usr/bin/python3

""" function that return json representation of an object"""

import json


def to_json_string(my_obj):
    """
    return json recpresenation of object
    """
    return json.dumps(my_obj)
