#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        aux = list(my_string)
        for i in range(aux.count('c')):
            aux.remove('c')
        
        for i in range(aux.count('C')):
            aux.remove('C')

        new = "".join(aux)
        return new
