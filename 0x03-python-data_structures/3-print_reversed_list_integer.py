#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list)
    for i in range(list_size):
        print("{:d}".format(my_list[list_size - i]))
