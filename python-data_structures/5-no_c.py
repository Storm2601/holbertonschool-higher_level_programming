#!/usr/bin/python3
def no_c(my_string):
    new_result = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_result += i
    return new_result
