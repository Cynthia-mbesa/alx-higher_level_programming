#!/usr/bin/python3
"""module that defines a function that
adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute, value):
    """adds new attribute to an object if possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
