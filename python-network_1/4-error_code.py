#!/usr/bin/python3
""" Error code #1
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP error status codes
        print(response.text)
    except requests.exceptions.HTTPError as err:
        print("Error code:", err.response.status_code)
