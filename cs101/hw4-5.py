#!/usr/bin/python
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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    while True:
        line = sys.stdin.readline()
        if line:
            print split_string(line,'\n ;,-()')
        else:
            break

