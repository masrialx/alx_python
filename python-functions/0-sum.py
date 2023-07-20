#!/usr/bin/python3
def add(a, b):
    return a + b

add = __import__('0-sum').add

print(f'[Got]      {add(1, 2)}')
print(f'[Expected] 3')
print()

print(f'[Got]      {add(98, 0)}')
print(f'[Expected] 98')
print()

print(f'[Got]      {add(100, -2)}')
print(f'[Expected] 98')

