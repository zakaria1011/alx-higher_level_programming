#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        int_printed = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end="")
            int_printed += 1
    except (TypeError, ValueError):
        continue
    return int_printed
