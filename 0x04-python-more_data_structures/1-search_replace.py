#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for s in range(len(my_list)):
        if my_list[s] == search:
            copy.append(replace)
        else:
            copy.append(my_list[s])
    return copy
