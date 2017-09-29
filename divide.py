#!/usr/bin/env python3

"""
Dividing integer numbers and
returning list [q, r]. Which are quotient and remainder, respectively.
"""

from sys import argv
from errorhandler import zerodiv, inputerror

def divide(a,b):
    try:
        q = a // b
    except ZeroDivisionError:
        zerodiv("b")
    r = a - b*q
    return [q,r]

if __name__ == "__main__":
    if len(argv) != 3:
        inputerror(2)
    try:
        a, b = int(argv[1]), int(argv[2])
    except ValueError:
        inputerror(2)

    [q,r] = divide(a,b)
    print("""
    a = %d, b = %d, q = %d, r = %d
    satisfy a = b*q + r
    """
    %(a,b,q,r))

