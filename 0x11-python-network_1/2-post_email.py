#!/usr/bin/python3
"""takes in URL and an email
sends a post request to passed URL
with the email as a parameter
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as r:
        print(r.read().decode('utf-8'))
