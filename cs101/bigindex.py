#!/usr/bin/python
import sys

def make_string(letters):
    s = ''
    for i in range(len(letters)):
        s = s + letters[i]
    return s

def make_big_index(size):
    index = []
    letters = ['a','a','a','a','a','a','a','a','a']
    while len(index) < size:
        word = make_string(letters)
        index.append(word)
        for i in range(len(letters)-1, 0, -1):
            if letters[i] < 'z':
                letters[i] = chr(ord(letters[i]) + 1)
                break;
            else:
                letters[i] = 'a'
    return index

if len(sys.argv) < 2:
    sys.exit(1)
n = int(sys.argv[1])
index = make_big_index(n)
print index


