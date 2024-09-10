#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = []
    unique = set(my_list)
    for i in unique:
        unique_int.append(i)
    return sum(unique_int)
