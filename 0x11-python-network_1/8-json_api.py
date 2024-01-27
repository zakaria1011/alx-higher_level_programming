#!/usr/bin/python3
""" json api """


if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = 'http://0.0.0.0:5000/search_user0'
    data = {'q': q}
    response = requests.post(url, data=data)

    try:
        json_data = response.read()
        if json_data == {}:
            print("No result")
        else:
            print("[{}] {}".format(json_data['id'], json_data['name']))
    except ValueError:
        print("Not a valid JSON")
