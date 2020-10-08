#!/usr/bin/python3
"""
Module 1-number_of_lines.py
"""


def number_of_lines(filename=""):
    """ returns the number of lines of a text file: """
    count = 0
    with open(filename, "r") as fp:
        lines = fp.readlines()
        for i in range(len(lines)):
            count += 1

    return count
