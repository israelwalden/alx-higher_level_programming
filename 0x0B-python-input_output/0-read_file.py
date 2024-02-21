#!/usr/bin/python3
""" Define a text file reading function """


def read_file(filename=""):
    """print the content of the file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
