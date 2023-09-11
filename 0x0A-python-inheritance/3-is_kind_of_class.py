#!/usr/bin/python3
"""a module that defines a function that returns
True if the object is an instance of, or if the object
is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """returns true or false

    Args: obj: the object to check
    a_class: the class to compare with
    """
    return isinstance(obj, a_class)
