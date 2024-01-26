#!/usr/bin/python3
""" fetch an url """


if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html_content = response.read()
        utf8_html_content = html_content.decode('utf8')
        print("Body response:")
        print("    - type:{}".format(type(html_content)))
        print("    - content:{}".format(html_content))
        print("    - utf8 content:{}".format(utf8_html_content))
