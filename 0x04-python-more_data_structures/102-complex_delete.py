#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_delet = []
    for key, val in a_dictionary.items():
        if val == value:
            key_to_delet.append(key)
    for key in key_to_delet:
        del a_dictionary[key]
