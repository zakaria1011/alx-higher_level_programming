#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if (sys.argv[2] == "+"):
        result = int(sys.argv[1]) + int(sys.argv[3])
        print("{} + {} = {}".format(sys.argv[1], sys.argv[3], result))
    elif (sys.argv[2] == "-"):
        result = int(sys.argv[1]) - int(sys.argv[3])
        print("{} - {} = {}".format(sys.argv[1], sys.argv[3], result))
    elif (sys.argv[2] == "*"):
        result = int(sys.argv[1]) * int(sys.argv[3])
        print("{} * {} = {}".format(sys.argv[1], sys.argv[3], result))
    elif (sys.argv[2] == "/"):
        result = int(sys.argv[1]) / int(sys.argv[3])
        print("{} / {} = {}".format(sys.argv[1], sys.argv[3], result))
    else :
        print("Unknown operator. Available operators: +, -, * and /")
