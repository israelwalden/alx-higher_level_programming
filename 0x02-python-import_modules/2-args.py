#!/usr/bin/python3
import sys

if __name__ == "__main__":
    cl_args = sys.argv
    if (len(cl_args) - 1) == 0:
        print("0 arguments")
    elif (len(cl_args) - 1) == 1:
        print("1 argument")
    else:
        print(f"{(len(cl_args) - 1):d} arguments:")
        for i in range(1, len(cl_args)):
            print(f"{i:d}: {cl_args[i]}")
