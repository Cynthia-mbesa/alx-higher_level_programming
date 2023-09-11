#!/usr/bin/python3
"""a module that defines a function that returns the list
of available attributes and methods of an object"""


def lookup(obj):
    """returns a list of available attributes and
    methods of an object"""
    return dir(obj)
