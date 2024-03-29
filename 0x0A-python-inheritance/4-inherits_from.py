#!/usr/bin/python3
"""a module that defines a function that returns True
if the object is an instance of a class that inherited
(directly or indirectly) from the specified class
otherwise False"""


def inherits_from(obj, a_class):
    """returns true or false

    Args: obj: the object to check
    a_class: the class to compare
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
