#!/usr/bin/env python
# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if len(text) == 0: return (0,0)
    last = len(text)
    text = text.lower()
    poly = []
    max_len = 1
    for i in range(len(text[:-1])):
        if text[i] == text[i+1]:
            poly.append((i,i+2))
    for i in range(len(text)):
        poly.append((i,i+1))
    #print "poly:",poly
    while True:
        expand = []
        for i,j in poly:
            if i > 0 and j < last:
                m,n = i-1,j+1
                if text[m] == text[n-1]:
                    expand.append((m,n))
        if expand:
            poly = expand
        else:
            break
    #print text,poly
    return poly[0]

def test():
    L = longest_subpalindrome_slice
    assert L('1 rr2') == (2, 4)
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'

print test()
