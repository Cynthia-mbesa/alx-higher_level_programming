#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    print a list of given integers

    Args:
    my_list (list of int, optional): The list of intergers to be printed.
    """
    if my_list is None:
        my_list = []

    for num in my_list:
        print("{:d}".format(num))
