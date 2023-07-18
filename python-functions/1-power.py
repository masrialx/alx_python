#!/usr/bin/python3
def pow(a, b):
    result = 1
    for x in range(b):
        result *= a
    return result
result = pow(2, 3)
print(result)