#!/usr/bin/python3
""" fetch variable from header but only using requests"""


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    content = response.headers.get('X-Request-Id')
    print(content)
