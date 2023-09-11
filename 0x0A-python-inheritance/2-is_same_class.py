#!/usr/bin/python3
"""module that defines a function that returns
True if the object is exactly an instance of the
specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """returns true or false

    Args: obj: the object to check
    a_class: the class to compare with
    """
    return type(obj) is a_class
