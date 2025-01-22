#!/usr/bin/python3
"""the function find_peak"""


def find_peak(list_of_integers):
    """finding a peak in a list of unsorted ints"""
    li = list_of_integers
    s = len(li)
    if s == 0:
        return
    r = s // 2
    if (r == s - 1 or li[r] >= li[r + 1]) and (r == 0 or li[r] >= li[r - 1]):
        return li[r]
    if r != s - 1 and li[r + 1] > li[r]:
        return find_peak(li[r + 1:])
    return find_peak(li[:r])
