#!/usr/bin/python3
"""
 fetch an url 
"""


if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html_content = response.read()
        print("Body response:")
        print("\t- type:{}".format(type(html_content)))
        print("\t- content:{}".format(html_content))
        print("\t- utf8 content:{}".format(html_content.decode('utf-8')))
