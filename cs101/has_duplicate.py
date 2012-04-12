#!/usr/bin/python
import time
import sys
import random

def has_duplicate_scan(p):
    """
    >>> has_duplicate_scan([2,4,3,1])
    False
    >>> has_duplicate_scan([2,4,3,2,1])
    True
    """
    for i in range(len(p)):
        for j in range(len(p)):
            if(i != j and p[i] == p[j]):
                return True
    return False

def has_duplicate_sort(p):
    """
    >>> has_duplicate_scan([2,4,3,1])
    False
    >>> has_duplicate_scan([2,4,3,2,1])
    True
    """
    p.sort()
    for i in range(len(p)-1):
        if(p[i] == p[i+1]):
            return True
    return False


def time_exec(code,n):
    start = time.clock()
    i = 0
    while i < n:
        result = eval(code)
        i += 1
    stop = time.clock()
    return result, (stop-start)*1000./n

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    n = 100
    if(len(sys.argv) > 1):
        n = int(sys.argv[1])
    vec = []
    for i in range(1,n):
        vec.append(random.randint(1,60*n))
    print vec
    res = time_exec('has_duplicate_sort(vec)',n)
    print "sort: ", res
    res = time_exec('has_duplicate_scan(vec)',n)
    print "scan: ", res
