#!/usr/bin/python3
from add_0 import add
a = 1
b = 2
result = a + b

print("{} + {} = {}".format(a, b, result))
if __name__ == "__main__":
    import sys
    add(int(sys.argv[1]), int(sys.argv[2]))
