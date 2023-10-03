#!/usr/bin/python3
def uppercase(str):
    uppercase_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - ord('a') + ord('A'))
            uppercase_str += uppercase_char
        else:
            uppercase_str += char
    print(uppercase_str)
