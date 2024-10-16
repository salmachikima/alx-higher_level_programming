#!/usr/bin/python3
"""
Contain fnct "write_file"
"""


def write_file(filename="", text=""):
    """return the number of char written to filename from text """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
