#!/usr/bin/python3
"""script fetches 'https://alx-intranet.hbtn.io/status'"""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request('https://alx-intranet.htbtn.io/status')
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body message:$")
        print("\t- type {}".format(type(body)))
        print("\t- content {}".format(body))
        print("\t- utf8 content {}".format(body.decode("utf-8")))