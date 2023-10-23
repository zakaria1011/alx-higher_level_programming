#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        integer_printed = 0
        for i in range(0, x):
            print("{:d}".format(my_list[i]), end="")
            integer_printed += 1
    except (ValueError, TypeError):
        continue
    print()
    return integer_printed
