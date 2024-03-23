#!/usr/bin/python3

for i in range(ord('a'), ord("z")):
    if (chr(i) != 'e' and chr(i) != 'q'):
        print("{}".format(chr(i)), end='')
