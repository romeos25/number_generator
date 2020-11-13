#!/usr/bin/env python3

import sys

file = open("number.lst", "w+")
num = int(sys.argv[1])
x = 0

for x in range(num):
    """if (x < 10):
        x = '$0'+str(x)+'\n'
    elif (x == num-1):
        x = '$'+str(x)
    else:
        x = '$'+str(x)+'\n'"""
    x = str(x)+'\n'
    file.write(x)

file.close()