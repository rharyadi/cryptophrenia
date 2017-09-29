#!/usr/bin/env python3

"""
Diffie Hellman key exchange
"""

from primechecker import primechecker
from sys import exit
from random import randint
from fastpower import fastpower

def generate_public_key(g,p):
    if not primechecker(p) or g>p or g<0:
        print("p should be prime and g is between 0 and p")
        exit(1)
    private_key = randint(0,p)
    public_key = fastpower(g,private_key,p)
    return [private_key, public_key]

def generate_shared_key(private_key, partner_public_key, p):
    shared_key = fastpower(partner_public_key, private_key, p)
    return shared_key


