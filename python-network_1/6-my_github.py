#!/usr/bin/python3
""" My GitHub
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))

    try:
        user_info = response.json()
        if "id" in user_info:
            print(user_info["id"])
        else:
            print("None")
    except ValueError:
        print("None")
