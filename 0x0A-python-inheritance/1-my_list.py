#!/usr/bin/python3
"""module that defines a class that inherits from list"""


class MyList(list):
    """the class defined by the module"""
    pass

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(list(self)))
