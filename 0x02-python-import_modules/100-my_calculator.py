#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    if op in operators:
        print("{} {} {} = {}".format(a, op, b, operators[op](a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
