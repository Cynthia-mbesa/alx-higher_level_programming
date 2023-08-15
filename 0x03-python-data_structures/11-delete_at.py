#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    a function that deletes the item at a specific position in a list.
    """
    l_len = len(my_list)
    if idx >= l_len or idx < 0:
        return (my_list)

    del my_list[idx]
    return (my_list)
