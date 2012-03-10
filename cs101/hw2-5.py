#!/usr/bin/python

import sys, random

def loop(n):
    i = 0
    while n != 1:
        i = i + 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return i

n = 1
while True:
    n = n + 1
    print n, "\t", "*" * 10,
    print loop(n)



