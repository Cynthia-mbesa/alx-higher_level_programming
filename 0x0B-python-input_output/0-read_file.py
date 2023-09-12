#!/usr/bin/python3
"""module for reading and printing contents of a file"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
