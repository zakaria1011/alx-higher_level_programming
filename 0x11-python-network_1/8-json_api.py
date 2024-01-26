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

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data['id'], json_data['name']))
        else:
            print("No result")
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print("No result")
        else:
            print("Not a valid JSON")
    except ValueError:
        print("Not a valid JSON")
