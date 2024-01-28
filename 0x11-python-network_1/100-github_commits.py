#!/usr/bin/python3
""" api git hub """


import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    repo_owner = sys.argv[2]

    api_url = 'https://developer.github.com/v3/repos/{}/{}/commits/'.format(
        repo_owner, repo_name)
    response = requests.get(api_url)
    commits = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
