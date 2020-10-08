#!/usr/bin/python3
"""
Module 2-read_lines.py
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        if nb_lines <= 0 or nb_lines == number_of_lines(filename):
            print(f.read(), end="")

        for i in range(nb_lines):
            if i < nb_lines:
                print(f.readline(), end="")


def number_of_lines(filename=""):
    """ returns the number of lines of a text file: """
    count = 0
    with open(filename, "r") as fp:
        lines = fp.readlines()
        for i in range(len(lines)):
            count += 1
    return count
