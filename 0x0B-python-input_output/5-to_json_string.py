#!/usr/bin/python3
"""
Module 5-to_json_string.py
"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object"""
    json_rep = json.dumps(my_obj)
    return json_rep
