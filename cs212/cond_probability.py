import itertools
from fractions import Fraction

sex = 'BG'

def product(*variables):
    return map(''.join, itertools.product(*variables))

two_kids = product(sex, sex)
print two_kids
one_boy = [s for s in two_kids if 'B' in s]
print one_boy

def two_boys(s): return s.count('B') == 2

def condP(predicate, event):
    pred = [s for s in event if predicate(s)]
    return Fraction(len(pred), len(event))

print condP(two_boys, one_boy)

day = 'SMTWtFs'

two_kids_bday = product(sex, day, sex, day)
#print two_kids_bday
one_boy_T = [s for s in two_kids_bday if 'BT' in s]
print one_boy_T

print condP(two_boys,one_boy_T)


