#!/usr/bin/python3
"""takes URL sends a request to the URL
displays the body of the response
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    s = requests.get(url)
    if s.status_code >= 400:
        print("Error code: {}".format(s.status_code))
    else:
        print(s.text)
