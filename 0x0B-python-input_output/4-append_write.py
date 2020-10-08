#!/usr/bin/python3
"""
Module 4-append_write.py
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file and
    Returns the number of characters added
    """
    with open(filename, mode="a") as f:
        chars_added = f.write(text)
    return chars_added
