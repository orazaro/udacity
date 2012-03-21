#!/usr/bin/python
import time
import sys

def split_string(source,splitlist):
    """
    >>> out = split_string("This is a test-of the,string separation-code!", " ,!-")
    >>> print out
    ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']
    >>> out = split_string("After  the flood   ...  all the colors came out."," .")
    >>> print out
    ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']
    """
    result = []
    length = len(source)
    i = 0
    while i < length:
        if splitlist.find(source[i]) != -1:
            i += 1
        else:
            j = i + 1
            while j < length and splitlist.find(source[j]) == -1:
                j += 1
            result.append(source[i:j])
            i = j
    return result

def func():
    split_string('a b;c,d-e.f',' ;,-.')
    

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
    print time_exec('func()',n)[1]
