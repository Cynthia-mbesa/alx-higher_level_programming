#!/usr/bin/python3
"""a module that appends"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    returns the number of characters added"""
    with open(filename, 'a', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count
