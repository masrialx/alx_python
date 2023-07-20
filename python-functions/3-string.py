#!/usr/bin/python3
def reverse_string(string):
    reversed_string = ""
    for char in string:
        reversed_string = char + reversed_string
    return reversed_string
input_string = "Hello, World!"
reversed_string = reverse_string(input_string)
print(reversed_string)

