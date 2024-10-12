#!/usr/bin/python3
"""
it Add two new lines after a set of chars
"""


def text_indentation(text):
    """it Prints text with added two newlines
    after thoe chars:
        {'.', '?', ':'}.
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
