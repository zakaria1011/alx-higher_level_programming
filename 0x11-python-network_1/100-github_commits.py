#!/usr/bin/python3
""" api git hub """


import requests
import sys

if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    api_url = 'https://developer.github.com/v3/repos/{}/{}/commits/'.format(
        repo_name, owner_name)
    try:
        response = requests.get(api_url)
        commits = response.json()[:10]
        for commit in reversed(commits):
            commit_sha = commit['sha']
            author_name = commit_info['author']['name']
            print('{}: {}'.foramt(commit_sha, author_name))
    except Exception as e:
        print("{}".format(e))
