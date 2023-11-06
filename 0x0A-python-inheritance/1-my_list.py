#!/usr/bin/python3

""" class inherit from list """


class MyList(list):
    """
    extend list built-in
    args : list
    """
    def print_sorted(self):
        """
        methode that print object
        return : sorted list
        """
        print(sorted(self))
