#!/usr/bin/env python3

from sys import exit

def inputerror(n):
    print("arguments should be %d of integer(s)" %n)
    exit(1)

def zerodiv(x):
    print("variable %s can not be zero" %x)
    exit(1)

def modzero():
    print("modular zero is undefined")
    exit(1)
