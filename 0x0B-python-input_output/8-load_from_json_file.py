#!/usr/bin/python3
"""
Module 8-load_from_json_file.py
"""


import json


def load_from_json_file(filename=""):
    """Creates an Object from a JSON file"""
    with open(filename) as fd:
        object_ = json.load(fd)

    return object_
