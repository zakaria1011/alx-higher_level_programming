#!/usr/bin/python3

""" from json representation to object """

import json


def from_json_string(my_str):
    """
    from json to obj
    """
    return json.loads(my_str)
