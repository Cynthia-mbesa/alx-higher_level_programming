#!/usr/bin/python3
"""module that returns dictionary description"""


def class_to_json(obj):
    """returns dictionary description

    Args: obj: an instance of a class
    """
    return obj.__dict__
