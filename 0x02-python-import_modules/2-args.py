#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    args_len = len(args)
    i = 1
    if args_len == 0:
        print("{:d} arguments.".format(args_len))
    elif args_len == 1:
        print("{:d} argument:".format(args_len))
        print("{:d}: {:s}".format(i, sys.argv[1]))
    else:
        print("{:d} arguments:".format(args_len))
        for i in range(1, args_len):
            print("{:d}: {:s}".format(i, sys.argv[i]))
