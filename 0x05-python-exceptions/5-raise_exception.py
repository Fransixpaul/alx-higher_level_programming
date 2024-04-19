#!/usr/bin/python3
def raise_exception():
    try:
        result = 1 + 'hello'
    except TypeError:
        raise TypeError("Adding integer to string is not allowed")
