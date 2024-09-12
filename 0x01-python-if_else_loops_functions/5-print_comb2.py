#!/usr/bin/python3
for s in range(100):
    if s < 99:
        print("{:02d}".format(s), end=", ")
    else:
        print(s)
