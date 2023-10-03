#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    char_list = list(str)
    del char_list[2]
    return "".join(char_list)
