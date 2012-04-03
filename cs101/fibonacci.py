#!/usr/bin/python

def fibonacci(n):
    '''
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(50)
    12586269025
    '''
    current, next = 0, 1
    for i in range(0,n):
        current, next = next, current+next
    return current

if __name__ == '__main__':
    import doctest
    doctest.testmod()
