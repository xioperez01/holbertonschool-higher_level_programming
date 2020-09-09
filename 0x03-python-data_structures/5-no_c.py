#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        aux = list(my_string)
        for i in range(len(my_string)):
            if i == 'c' or i == 'C':
                aux.remove(i)

        aux = "".join(aux)
        return aux
