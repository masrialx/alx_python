#!/usr/bin/env python3
validate_password = __import__('6-password').validate_password

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123"))
