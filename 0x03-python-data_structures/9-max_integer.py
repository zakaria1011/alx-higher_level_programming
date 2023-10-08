#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_num = 0
    for value in my_list:
        if value > max_num:
            max_num = value
    return max_num
