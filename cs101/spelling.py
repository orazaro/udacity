#!/usr/bin/python
import sys
#Spelling Correction

#Double Gold Star

#For this question, your goal is to build a step towards a spelling corrector,
#similarly to the way Google used to respond,

#    "Did you mean: audacity"


#when you searched for "udacity" (but now considers "udacity" a real word!).

#One way to do spelling correction is to measure the edit distance between the
#entered word and other words in the dictionary.  Edit distance is a measure of
#the number of edits required to transform one word into another word.  An edit
#is either: (a) replacing one letter with a different letter, (b) removing a
#letter, or (c) inserting a letter.  The edit distance between two strings s and
#t, is the minimum number of edits needed to transform s into t.

#Define a procedure, edit_distance(s, t), that takes two strings as its inputs,
#and returns a number giving the edit distance between those strings.

#Note: it is okay if your edit_distance procedure is very expensive, and does
#not work on strings longer than the ones shown here.

#The built-in python function min() returns the mininum of all its arguments.

#print min(1,2,3)
#>>> 1

def gen_remove(s):
    steps = []
    for i in range(len(s)):
        l,r = s[:i], s[i+1:]
        steps.append(l+r)
    return steps


def gen_insert(s,t):
    #alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    steps = []
    for i in range(len(s)+1):
        l,r = s[:i], s[i:]
        #for c in t:
        #   steps.append(l+c+r)
        if len(t) > i:
            steps.append(l+t[i]+r)
    return steps

def gen_replace(s,t):
    steps = []
    for i in range(len(s)):
        l,r = s[:i],s[i+1:]
        if len(t) > i:
            steps.append(l+t[i]+r)
    return steps

def gen_steps(s,t):
    steps = []
    if len(s) >= len(t):
        steps = steps + gen_remove(s)
    if len(s) < len(t):
        steps = steps + gen_insert(s,t)
    steps = steps + gen_replace(s,t)
    return steps

def edit_distance(s,t):
    expanded = {}
    frontier = [s]
    dist = 0
    while frontier:
        p = []
        for k in frontier:
            if k == t:
                return dist
            if k not in expanded:
                expanded[k] = dist
                p = p + gen_steps(k,t)
        frontier = p
        dist += 1



print 'remove: 12CcCa'
print gen_remove('12CcCa')
print 'insert to "12" from "abs"'
print gen_insert('12','abc')
print 'replace to "12" from "abs"'
print gen_replace('12','abc')


#For example:

a,b='1234','54321'
print a,"->",b," d=",edit_distance(a,b)


# Delete the 'a'
print edit_distance('audacity', 'udacity')
#>>> 1

# Delete the 'a', replace the 'u' with 'U'
print edit_distance('audacity', 'Udacity')
#>>> 2

# Five replacements
print edit_distance('peter', 'sarah')
#>>> 5

# One deletion
print edit_distance('pete', 'peter')
#>>> 1


def test():
    t=[
            ['audacity',        'udacity',      1],
            ['audacity',        'Udacity',      2],
            ['peter',           'sarah',        5],
            ['pete',            'peter',        1],
            #['udc',             'audacity',     5],
            ['audacity',        'udc',          5],
            ['audacity',        'udacious',     4],
            ['python',          'pytohn',       2],
            ['udacity',         'university',   6],
            ['university',      'udacity',      6],
            ['edata',           'database',     5],
            ['smothered',       'moth',         5],
            ['moth',            'smothered',    5],
            ['smothered',       'other',        4],
            ['other',           'smothered',    4],
            ['the',             'smothered',    6],
            ['smothered',       'the',          6],
            ['there',           'smothered',    4],
            ['smothered',       'there',        4],
            ['horror',          'mirror',       2],
            ['beehive',         'behave',       2],
            ['audacity',        'xurdrity',     4],
            ['A man, a plan, a canal - Panama!',        'Doc, note: I dissent. A fast never prevents a fatness. I diet on cod.',        54],
            ['amanaplanacanalpanama',        'docnoteidissentafastneverpreventsafatnessidietoncod',        42],
            ['klebsiella pneumonia',        'salivating puma',        15]
        ]
    for y in t:
        print "edit_distance('",y[0],"','",y[1],"') = ",edit_distance(y[0],y[1]),y[2]

test()
