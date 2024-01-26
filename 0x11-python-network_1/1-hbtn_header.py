#!/usr/bin/python3
""" display value of variable in header """


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print("{}".format(response.headers.get('X-Request-Id')))
