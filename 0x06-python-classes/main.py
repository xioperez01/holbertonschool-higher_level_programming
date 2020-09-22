#!/usr/bin/python3
stack = []
def main():
    import sys
    get_fun = {"push": push, "pall": pall}
    file = str(sys.argv[1])
    with open(file, "r") as fd:
        line_number = 1
        for line in fd:
            op = line.split()
            print(op)
            get_fun[op[0]](op[1])
            print(line_number)
            line_number += 1

def push(val):
    stack.append(val)

def pall(val):
    print(*stack, sep = "\n")
    #for element in stack:
     #   print(element)
main()
