#!/usr/bin/env python
# ---------------
# User Instructions
#
# Write a function, n_ary(f), that takes a binary function (a function
# that takes 2 inputs) as input and returns an n_ary function. 

def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    def n_ary_f(x, *args):
        print 'f=',f
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f

def foo(a,b):
    return a + b

foo = n_ary(foo)
print 'foo=',foo
print foo(1,2,3,4,5)
g = n_ary(foo)
print 'g=',g
print foo(1,2,3,4,5)
