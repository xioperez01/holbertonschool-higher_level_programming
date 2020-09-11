#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) == str:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        imput_rev = reversed(roman_string)
        aux = 0
        aux_2 = 0
        for i in imput_rev:
            if num[i] >= aux_2:
                aux = aux + num[i]
            elif num[i] < aux_2:
                aux = aux - num[i]
            aux_2 = num[i]
        return aux
    else:
        return 0
