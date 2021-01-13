#!/usr/bin/python3
"""
Module that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in
the response header with requests and sys packages
"""

from sys import argv
import requests

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
