#!/usr/bin/python3
"""
Module 3-write_file.py
"""


def write_file(filename="", text=""):
    """ Writes a string to a text file and
    Returns the number of characters writen
    """
    with open(filename, mode="w") as f:
        num_char = f.write(text)
    return num_char
