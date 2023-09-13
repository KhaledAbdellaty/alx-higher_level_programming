#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    key = None
    score = 0
    for k, v in a_dictionary.items():
        if v > score:
            key = k
            score = v
    return key
