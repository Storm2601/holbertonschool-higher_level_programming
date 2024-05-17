#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for i in range(x):
        try:
            if num >= x:
                break
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (TypeError, ValueError):
            try:
                continue
            except IndexError:
                break
    print()
    return num
