#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    replace an element at a specific position in a list.

    Args:
    my_list (list): The list in which to replace the element.
    idx (int): The index at which to replace the element.
    element: The new element to replace with.

    Returns:
    Modified list if idx=valid, original list otherwise
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
