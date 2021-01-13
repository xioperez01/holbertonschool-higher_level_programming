#!/usr/bin/python3
"""
Module that uses Github API to list the last 10
commits of a given repository
"""

from sys import argv
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1])
    r = requests.get(url)
    commits = r.json()
    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
