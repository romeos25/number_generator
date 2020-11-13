#!/usr/bin/env python3

import sys

name = str(sys.argv[1])
file = open(name, 'w+')
num = int(sys.argv[2])
x = 0

for x in range(num):

    if (x > num):
        break
    x = str(x)+'\n'
    file.write(x)

file.close()