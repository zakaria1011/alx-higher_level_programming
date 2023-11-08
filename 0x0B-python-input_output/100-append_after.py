#!/usr/bin/python3

"""fonction insert text after specific string"""


def append_after(filename="", search_string="", new_string=""):
""" insert text """
    file_lines = []
    with open(filename, 'r') as file:
        file_lines = file.readlines()

    new_file_lines = []
    for line in file_lines:
        new_file_lines.append(line)
        if search_string in line:
            new_file_lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(new_file_lines)
