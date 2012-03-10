#!/usr/bin/python
import random, sys

def median(a,b,c):
    if a >= b:
        if c >= a:
            return a
        if b >= c:
            return b
        return c
    if c >= b:
        return b
    if c >= a:
        return c
    return a

while True:
    a = random.randint(1,10)
    b = random.randint(1,10)
    c = random.randint(1,10)
    print a, b, c
    print median(a,b,c)
    sys.stdin.read()

