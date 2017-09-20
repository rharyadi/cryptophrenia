#!/usr/bin/env python3

"""
Implement Fast Powering Algorithm using binary expansion
"""

from sys import argv
from errorhandler import *

def dec2bin(A):
    return "{0:b}".format(A)

def fastpower(g,A,n):
    if not n:
        modzero()
    if not A:
        return 1
    if A == 1:
        return g
    Abin_reverse = dec2bin(A)[::-1]
    current_power = g
    result = 1
    for i in Abin_reverse[1:]:
        current_power = current_power**2
        if i == '1':
            result = (result*current_power) % n
    return result

if __name__ == '__main__':
    if len(argv) != 4:
        inputerror(3)
    try:
        g,A,n = int(argv[1]), int(argv[2]), int(argv[3])
    except ValueError:
        inputerror(3)
    result = fastpower(g,A,n)
    print("%d ^ %d mod %d = %d" %(g,A,n,result))
