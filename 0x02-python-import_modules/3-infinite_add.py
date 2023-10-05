#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    result = 0
    for index in range(1, argv_count + 1):
        result += int(sys.argv[index])
    print("{:d}".format(result))
