#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    list_string = list(my_string)
    new_list = [x for x in list_string if x != 'c' and x != 'C']
    new_string = ''.join(new_list)
    return new_string
