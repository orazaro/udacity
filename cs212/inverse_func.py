#!/usr/bin/env python
# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the 
# non-negative numbers. The runtime of your program should be 
# proportional to the LOGARITHM of the input. You may want to 
# do some research into binary search and Newton's method to 
# help you out.
#
# This function should return another function which computes the
# inverse of the input function. 
#
# Your inverse function should also take an optional parameter, 
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The 
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is 
# efficient enough. 

def slow_inverse(f, delta=1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x = 0
        while f(x) < y:
            x += delta
        # Now x is too big, x-delta is too small; pick the closest to y
        return x if (f(x)-y < y-f(x-delta)) else x-delta
    return f_1 

def inverse(f, delta = 1/1280.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def f_1(y):
        x1 = 0.
        x2 = 2.
        while f(x2) < y:
            x2 = x2 * x2
        while True:
            if abs(y - f(x1)) < delta: return x1
            if abs(y - f(x2)) < delta: return x2
            x = (x1 + x2) / 2.
            if f(x) < y:
                x1 = x
            else:
                x2 = x
    return f_1

    
def square(x): return x*x
sqrt = slow_inverse(square)
sqrt = inverse(square)

n = 10000000123456.
print "%20.f" % (sqrt(n)*sqrt(n))

