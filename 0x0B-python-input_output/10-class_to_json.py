#!/usr/bin/python3
"""
Module 10-class_to_json.py
"""


def class_to_json(obj):
    """Returns the dict representation of class for JSON
    serialization"""

    return (getattr(obj, "__dict__"))
