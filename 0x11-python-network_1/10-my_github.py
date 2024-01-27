#!/usr/bin/python3
"""

"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user' 

    try:
        response = requests.get(url, auth=(username, token))
        json_data = response.json()
        
        if 'id' in json_data:
            print(json_data['id'])
        else:
            print("None")
    except ValueEroor:
        print("None")