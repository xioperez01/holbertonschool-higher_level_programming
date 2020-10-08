#!/usr/bin/python3
"""
Module  6-from_json_string.py
"""


import json


def from_json_string(my_str):
    """Converts ths json string to object"""
    object_by_str = json.loads(my_str)
    return object_by_str
