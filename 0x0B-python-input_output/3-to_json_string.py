#!/usr/bin/python3
"""module that returns the JSON
representation of an object (string)"""
import json


def to_json_string(my_obj):
    """returns JSON representation"""
    return json.dumps(my_obj)
