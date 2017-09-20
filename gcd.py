#!/usr/bin/env python3

"""
Calculating gcd of given numbers
"""

from sys import argv
from divide import divide
from errorhandler import inputerror, zerodiv

def gcd(a,b):
    try:
        [q, r] = divide(a,b)
    except ZeroDivisionError:
        zerodiv("b")
    while True:
        [q, r] = divide(a,b)
        if not r:
            break
        a,b = b,r
    return b

if __name__ == "__main__":
    if len(argv) != 3:
        inputerror(2)
    try:
        a,b = int(argv[1]), int(argv[2])
    except:
        inputerror(2)

    g = gcd(a,b)
    print("a = %d, b = %d, gcd(a,b) = %d" %(a,b,g))
