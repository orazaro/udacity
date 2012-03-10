#!/usr/bin/python
import random, sys

g = 0
def test(a):
    global g
    if a > g:
        g += 1
        return True
    else:
        return False

def proc1(a, b):
    if test(a):
        return b
    return a

def proc4(a,b):
    if not test(a):
        b = 'udacity'
    else:
        return b
    return a

while(True):
    g_old = g
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    r1 = proc1(a, b)
    g1 = g
    g = g_old
    r2 = proc4(a, b)
    if(r1 == r2 and g1 == g):
        sys.stdout.write('.')
    else:
        print '\nerror detected for ', a, b, g1, g
        break

