#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list) - 1
    for i in range(list_size + 1):
        print("{}".format(my_list[list_size - i]))
