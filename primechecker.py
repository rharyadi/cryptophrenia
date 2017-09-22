#!/usr/bin/env python3

"""
Checking if a number is a prime using Fermat Little Theorem
which states that for prime number p, this condition applies
a^(p-1) = 1 (mod p)
Here, we use a=2
"""

from sys import argv
from errorhandler import *
from fastpower import fastpower

def primechecker(p):
    if not p:
        modzero()
    congruence = fastpower(2,p-1,p)
    if congruence == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    if len(argv) != 2:
        inputerror(1)
    try:
        p = int(argv[1])
    except ValueError:
        inputerror(1)
    checkresult = primechecker(p)
    if checkresult:
        print("%d is prime" %p)
    else:
        print("%d is not prime" %p)

