#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        aux = list(my_string)
        for i in range(len(my_string)):
            if my_string[i] == 'c' or my_string[i] == 'C':
                aux.remove(aux[i])

        aux = "".join(aux)
        return aux
