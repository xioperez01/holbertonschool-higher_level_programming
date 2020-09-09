#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        aux = list(my_string)
        for i in aux:
            if i == 'c' or i == 'C':
                aux.remove(i)

        aux = "".join(aux)
        return aux
