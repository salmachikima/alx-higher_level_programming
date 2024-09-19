#!/usr/bin/python3
def magic_calculation(s, r):
    from magic_calculation_102 import add, sub
    if s < r:
        c = add(s, r)
        for n in range(4, 6):
            c = add(c, n)
        return c
    else:
        return sub(s, r)
