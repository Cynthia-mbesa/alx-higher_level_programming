#!/usr/bin/python3
"""101-locked_class - defines a class LockedClass"""


class LockedClass:
    """class representing LockedClass"""
    def __setattr__(sel, name, value):
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                    "'LockedClass' object has no attribute '{}'".format(name))
