#!/usr/bin/python3
"""
Checks student output for returning info from REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"


def check_tasks(id):
    """ Fetch user name, number of tasks """

    resp = requests.get(todos_url).json()

    filename = 'student_output'
    count = 0
    with open(filename, 'r') as f:
        next(f)  # Skip the first line
        for line in f:
            count += 1
            # Remove leading and trailing whitespace before checking formatting
            line = line.strip()
            if line.startswith('\t') and line.count('\t') == 1 and line.endswith('\n'):
                print("Task {} Formatting: OK".format(count))
            else:
                print("Task {} Formatting: Incorrect".format(count))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 check_format.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    check_tasks(employee_id)
