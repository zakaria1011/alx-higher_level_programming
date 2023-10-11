#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = []
    mult_by_num = lambda x: x * number
    new_list = list(map(mult_by_num, my_list))
    return new_list
