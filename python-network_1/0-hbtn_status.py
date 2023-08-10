#!/usr/bin/python3
"""
Fetches https://alu-intranet.hbtn.io/status using requests package.
"""

import requests

if __name__ == "__main__":
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
