#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL
and displays the body of the response
"""

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    try:
        url = argv[1]
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
