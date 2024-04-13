#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_with_value = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_with_value.append(key)
    for key in keys_with_value:
        del a_dictionary[key]
    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
