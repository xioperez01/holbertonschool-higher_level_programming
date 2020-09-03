#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    imput = len(sys.argv) - 1

    if imput == 1:
        print("{} argument:".format(imput))
    elif imput == 0:
        print("{} arguments.".format(imput))
    else:
        print("{} arguments:".format(imput))

    for i in range(imput):
        print("{}: {}".format(i + 1, str(sys.argv[i + 1])))
