#!/usr/bin/python3
"""
Created on 12/10/2020

@author: xioperez
"""


import json


class Base(object):
    """ class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    """def save_to_file(cls, list_objs):"""

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of the JSON string
        representation json_string:
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
