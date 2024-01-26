#!/usr/bin/python3
""" post email using only requests"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)

    content = response.json()
    email_from_response = content.get('email')
    print("Your email is: {}".format(email_from_response))
