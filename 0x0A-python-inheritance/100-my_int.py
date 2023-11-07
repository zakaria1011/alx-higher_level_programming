#!/usr/bin/python3

""" myint inheret from int  """


class MyInt(int):
    """class my int  """
    def __eq__(self, other):
        """ Override the equality operator (==) """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Override the inequality operator (!=) """
        return super().__eq__(other)
