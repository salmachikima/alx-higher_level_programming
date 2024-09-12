#!/usr/bin/python3
for s in range(0, 9):
    for r in range(s + 1, 10):
        if s == 8:
            print("{}{}".format(s, r))
        else:
            print("{}{}".format(s, r), end=", ")
