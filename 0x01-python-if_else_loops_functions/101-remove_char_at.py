#!/usr/bin/python3
def remove_char_at(str, s):
    if 0 <= s < len(str):
        return (str.replace(str[s], ""))
    else:
        return (str)
