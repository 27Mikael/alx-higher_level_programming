#!/usr/bin/python3
"""send POST to url with email as parameter, displays response body"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.REQUEST(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utd-8"))
