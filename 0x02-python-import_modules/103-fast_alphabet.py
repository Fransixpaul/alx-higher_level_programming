#!/usr/bin/python3
import string
print(bytes(getattr(string, 'ascii_uppercase'), 'utf-8').decode('utf-8'))
