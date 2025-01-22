#!/usr/bin/python3
"""takes in a URL sends a request to the URL
displays the value of the variable X-Request-Id
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
