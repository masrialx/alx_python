#!/usr/bin/env python3
def no_c(my_string):
    result = ""
    i = 0
    while i < len(my_string):
        if my_string[i].lower() == 'c':
            i += 1
        else:
            result += my_string[i]
            i += 1
    return result

# Test cases
print(no_c("Holberton School"))  # Output: "Holberton School"
print(no_c("Chicago"))           # Output: "hiago"
print(no_c("C is fun!"))         # Output: " is fun!"
       
