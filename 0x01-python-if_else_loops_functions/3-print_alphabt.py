#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i is (ord('e')) or i is (ord('q')):
        continue
    print("{}".format(chr(i)), end="")
