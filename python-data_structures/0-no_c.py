#!/usr/bin/python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            result += char
    return result
print(no_c("Holberton School"))  # Output: "Holberton Shool"
print(no_c("Chicago"))          # Output: "hiago"
print(no_c("C is fun!"))        # Output: " is fun!"
