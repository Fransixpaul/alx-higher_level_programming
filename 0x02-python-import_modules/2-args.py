#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name itself

    if num_args == 0:
        print("0 argument(s).")
        print(".")
    else:
        print(f"{num_args} argument{'s' if num_args > 1 else ''}:")
        for idx, arg in enumerate(argv[1:], start=1):
            print(f"{idx}: {arg}")
