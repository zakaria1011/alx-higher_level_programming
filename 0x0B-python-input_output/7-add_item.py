#!/usr/bin/python3

"""add arg to python list and save them in a file"""

import sys
import os
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

args_list = []
json_file = 'add_item.json'
if os.path.exists(json_file):
    args_list = load_from_json_file(json_file)
args_list.extend(sys.argv[1:])
args_list.extend(sys.argv[1:])
