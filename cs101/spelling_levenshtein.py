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

def levenshtein(s,t,i,j,lev):
    if i == 0:
        return j
    if j == 0:
        return i
    key = str(i) + '-' + str(j)
    if key in lev:
        return lev[key]
    d1 = 1 + levenshtein(s,t,i-1,j,lev)
    d2 = 1 + levenshtein(s,t,i,j-1,lev)
    if s[i-1] == t[j-1]:
        d3 = levenshtein(s,t,i-1,j-1,lev)
    else:
        d3 = 1 + levenshtein(s,t,i-1,j-1,lev)
    lev[key] = min(d1,d2,d3)
    return lev[key]


def edit_distance(s,t):
    lev = {}
    return levenshtein(s,t,len(s),len(t),lev)

#For example:


def test():
    t=[
            ['audacity',        'udacity',      1],
            ['audacity',        'Udacity',      2],
            ['peter',           'sarah',        5],
            ['pete',            'peter',        1],
            ['udc',             'audacity',     5],
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
