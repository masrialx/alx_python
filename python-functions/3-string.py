#!/usr/bin/env python3
def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("madam"))
print(reverse_string("Hello, World!"))

