#!/usr/bin/python3
def uniq_add(my_list=[]):
    list_unique = []
    unique = set(my_list)
    for i in unique:
        list_unique.append(i)
    return sum(list_unique)
