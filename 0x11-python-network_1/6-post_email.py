#!/usr/bin/python3
"""Uses request to get POST and email to URL"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, data=value)
    print(req.text)
