#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status
like the 0 task
"""
if __name__ == "__main__":
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    response = req.text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
