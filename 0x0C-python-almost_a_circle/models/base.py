#!/usr/bin/python3
'''
Created on 12/10/2020

@author: xioperez
'''


class Base(object):
    '''
    class Base
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
