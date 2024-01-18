#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    cl_args = sys.argv
    if len(cl_args)-1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    op = cl_args[2]
    if op != "+" and op != "-" and op != "*" and op != "/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(cl_args[1])
    b = int(cl_args[3])

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
        sys.exit(0)
    elif op == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
        sys.exit(0)
    elif op == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
        sys.exit(0)
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
        sys.exit(0)
