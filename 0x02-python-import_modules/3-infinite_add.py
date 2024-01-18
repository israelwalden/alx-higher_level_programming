#!/usr/bin/python3
import sys
if __name__ == "__main__":

    cl_args = sys.argv
    total = 0
    for i in range(1, len(cl_args)):
        total = total + int(cl_args[i])
    print("{}".format(total))
