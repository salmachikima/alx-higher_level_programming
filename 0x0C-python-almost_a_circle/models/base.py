#!/usr/bin/python3
'''base class module'''
from json import dumps, loads
import csv


class Base:
    '''representation of base of our OOP hierarchy'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
