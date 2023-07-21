#!/usr/bin/python3
import sys


num_args = len(sys.argv) - 1


if num_args == 0:
    print("0 arguments.")
else:
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    for i, arg in enumerate(sys.argv[1:], 1):
        print(f"{i}: {arg}")

