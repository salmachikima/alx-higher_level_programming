#!/usr/bin/python3
for s in range(122, 96, -1):
    char = s
    if s % 2 != 0:
        char = char - 32
    print("{:c}".format(char), end="")
