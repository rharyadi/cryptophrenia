#!/usr/bin/env python3

"""
Computing Euler Phi Function / Totient function
that is phi(n) is the counts of positive integers up to n
that are coprime to n, or gcd(n,k) = 1
I don't know yet if there is a better way,
but for now, I'll simply use bruteforce
"""

from sys import argv
from errorhandler import *
from gcd import gcd

def naiveeulerphi(n):
    count = 0
    # n itself is excluded in this loop, since gcd(n,n) = n
    for k in range(1,n):
        if gcd(n,k) == 1:
            count = count + 1
    return count

if __name__ == "__main__":
    if len(argv) != 2:
        inputerror(1)
    try:
        n = int(argv[1])
    except ValueError:
        inputerror(1)

    phi = naiveeulerphi(n)
    print("phi(%d) = %d" %(n,phi))
