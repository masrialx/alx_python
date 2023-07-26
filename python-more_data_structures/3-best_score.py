#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    max_value = None
    best_key = None

    for key, value in a_dictionary.items():
        if max_value is None or value > max_value:
            max_value = value
            best_key = key

    return best_key
