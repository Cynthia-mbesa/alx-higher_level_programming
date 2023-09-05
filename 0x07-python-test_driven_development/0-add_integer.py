#!/usr/bin/python3
def add_integer(a, b=98):
    """ adds two integers

    Args: a(int or float), first number
    b(int or float), second number
    Returns: sum of the two numbers
    Raises: TypeError if a or b is not float or int
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
