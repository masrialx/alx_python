#!/usr/bin/python3
a = 1
b = 2

from add_0 import add

result = add(a, b)

if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, result))