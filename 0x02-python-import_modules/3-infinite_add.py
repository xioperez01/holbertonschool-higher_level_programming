#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    imput = len(sys.argv) - 1
    add_ = 0
    for i in range(imput):
        add_ += int(sys.argv[i + 1])

    print("{}".format(add_))
