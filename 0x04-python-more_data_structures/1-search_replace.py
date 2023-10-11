#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x in new_list:
        if x == search:
            idx = new_list.index(x)
            new_list[idx] = replace
    return new_list
