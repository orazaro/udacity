#!/usr/bin/python
import time
import sys

def time_exec(code):
    start = time.clock()
    result = eval(code)
    stop = time.clock()
    return result, stop-start

def func(n):
    while n:
        n -= 1

if __name__ == '__main__':
    n = 100
    if(len(sys.argv) > 1):
        n = int(sys.argv[1])
    print time_exec('func(n)')[1] * 1000. / n
