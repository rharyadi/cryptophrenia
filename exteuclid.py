#!/usr/bin/env python3

"""
Extended Euclidean Algorithm.
Given two integers a,b, solving au+bv=gcd(a,b)
then returning [u,v]
"""

from divide import divide
from errorhandler import zerodiv, inputerror
from sys import argv

def exteuclid(a,b):
    try:
        [q,r] = divide(a,b)
    except ZeroDivisionError:
        zerodiv("b")

    matrix = [[0,0],[0,1],[1,0]]
    wc = 2 # current working column
    while True:
        [q, r] = divide(a,b)
        matrix[0].append(q)
        matrix[1].append(matrix[0][wc]*matrix[1][wc-1] + matrix[1][wc-2])
        matrix[2].append(matrix[0][wc]*matrix[2][wc-1] + matrix[2][wc-2])

        if not r:
            break
        a,b = b,r
        wc = wc + 1

    u = matrix[2][-2]
    v = -matrix[1][-2]

    return [u,v]

if __name__ == "__main__":
    if len(argv) != 3:
        inputerror(2)
    
    try:
        a,b = int(argv[1]), int(argv[2])
    except:
        inputerror(2)

    u,v = exteuclid(a,b)

    print("""
    a = %d, b = %d, u = %d, v = %d
    will satisfy au+bv = gcd(a,b)
    """
    %(a,b,u,v))

