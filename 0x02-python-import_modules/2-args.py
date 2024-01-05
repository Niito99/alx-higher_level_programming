#!/usr/bin/python3
from sys import argv

if len(argv) == 1:
    print("{} arguments.".format(len(argv) - 1))
elif len(argv) == 2:
    print("{} argument: \n1: {}".format((len(argv) - 1), argv[1]))

else:
    print("{} arguments:".format(len(argv) - 1))
    for i in range(len(argv)):
        if i == 0:
            continue
        print("{}: {}".format(i, argv[i]))
