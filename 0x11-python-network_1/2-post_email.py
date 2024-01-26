#!/usr/bin/python3
""" post email using only requests"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    response = requests.post(url, data=data)
    
    # Assuming the server returns JSON and has the email field
    try:
        content = response.json()
        email_from_response = content.get('email')
        print("Your email is: {}".format(email_from_response))
    except ValueError:
        print("Failed to parse JSON response. Response content:")
        print(response.text)
