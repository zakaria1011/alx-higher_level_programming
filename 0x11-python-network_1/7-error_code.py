#!/usr/bin/python3
""" fetch url with error rise """


if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))

