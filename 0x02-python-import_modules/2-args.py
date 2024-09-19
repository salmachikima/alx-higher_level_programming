#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = len(sys.argv) - 1

    if s == 0:
        print("{} arguments.".format(s))
    elif s == 1:
        print("{} argument:".format(s))
    else:
        print("{} arguments:".format(s))

    if s >= 1:
        s = 0
        for arg in sys.argv:
            if s != 0:
                print("{}: {}".format(s, arg))
            s += 1
