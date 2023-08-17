#!/usr/bin/python3
def best_score(a_dictionary):
    """
    a function that returns a key with the biggest integer value
    You can assume that all values are only integers
    If no score found, return None
    You can assume all students have a different score
    """
    win_n = 0
    winner = None
    if type(a_dictionary) is dict:
        for (key, value) in a_dictionary.items():
            if value > win_n:
                win_n = value
                winner = key
    return winner
