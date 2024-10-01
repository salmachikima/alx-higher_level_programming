#!/usr/bin/python3
def magic_calculation(a, b):
    r = 0
    for s in range(1, 3):
        try:
            if s > a:
                raise Exception("Too far")
            r += (a ** b) / s
        except Exception:
            r = b + a
            break
    return r
