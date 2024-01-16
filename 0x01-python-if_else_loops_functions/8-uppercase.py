#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            letter = chr(ord(i) - 32)
        else:
            letter = chr(ord(i))
        print("{}".format(letter), end="")
    print("")
