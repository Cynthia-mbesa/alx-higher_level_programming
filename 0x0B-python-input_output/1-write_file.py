#!/usr/bin/python3
"""module that writes a string into a text file"""


def write_file(filename="", text=""):
    """writes a string into text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        char_count = file.write(text)
    return char_count
