#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[1:]
    argc = len(argv)

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
 
    a, b, opr = int(argv[0]), int(argv[2]), argv[1]
    if opr == "+":
        print("{} {} {} = {}".format(a, opr, b, add(a, b)))
    elif opr == "-":
        print("{} {} {} = {}".format(a, opr, b, sub(a, b)))
    elif opr == "*":
        print("{} {} {} = {}".format(a, opr, b, mul(a, b)))
    elif opr == "/":
        print("{} {} {} = {}".format(a, opr, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
