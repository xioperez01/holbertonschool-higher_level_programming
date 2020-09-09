#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    i = 0
    while i < len(my_list):
        if my_list[i] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
            i+= 1

    return new
