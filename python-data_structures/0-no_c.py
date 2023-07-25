#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    for char in my_string:
        if char.lower() != 'c':
            result += char
    return result


print(no_c("Holberton School")) 
print(no_c("Chicago"))          
print(no_c("C is fun!"))         
