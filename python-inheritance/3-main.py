#!/usr/bin/python3
BaseGeometry = __import__('3-base_geometry').BaseGeometry

bg = BaseGeometry()

print(bg)
print(sorted(dir(bg)))  # Sort the attributes before printing
print(sorted(dir(BaseGeometry)))  # Sort the attributes before printing
