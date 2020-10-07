#!/usr/bin/python3
"""
Module 1-my_list.py
"""


class MyList(list):
    """ class MyList that inherits from list """
    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        print(sorted(self))
