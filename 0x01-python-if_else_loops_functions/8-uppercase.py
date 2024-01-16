#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            l = chr(ord(i) - 32)
        else:
            l = chr(ord(i))
        print("{}".format(l), end="")
    print("")
