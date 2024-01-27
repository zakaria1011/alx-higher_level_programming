#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user id.
"""

import requests
import sys

if __name__ == "__main__":
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

    except ValueError:
        print("None")
