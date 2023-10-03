#!/usr/bin/python3
for char_code in range(ord('z'), ord('a'), -2):
    print("{}".format(chr(char_code)), end="")
    print("{}".format(chr(char_code - 33)), end="")
