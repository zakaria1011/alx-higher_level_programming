#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return None
    list_string = list(sentence)
    leng_of_string = len(list_string)
    return (leng_of_string, list_string[0])
