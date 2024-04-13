#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_score = max(a_dictionary.values())
    best_keys = []

    for key, value in a_dictionary.items():
        if value == max_score:
            best_keys.append(key)

    return best_keys[0]
