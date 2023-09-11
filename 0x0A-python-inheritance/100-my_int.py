#!/usr/bin/python3
"""module that defines that inherits from int"""


class MyInt(int):
    """class defined"""

    def __eq__(self, other):
        """override == operator to return inverted results"""
        return super().__ne__(other)

    def __ne__(self, other):
        """override != operator to return inverted result"""
        return super().__eq__(other)
