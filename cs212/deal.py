# -----------
# User Instructions
# 
# Write a function, deal(numhands, n=5, deck), that 
# deals numhands hands with n cards each.
#

import random # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the 
# Instructor Comments box below).

mydeck = [r+s for r in '23456789TJQKA' for s in 'SHDC'] 

def shuffle(deck):
    n = len(deck)
    for m in range(n):
        i = random.randint(0,n-1)
        j = random.randint(0,n-1)
        deck[i], deck[j] = deck[j], deck[i]

#def deal(numhands, n=5, deck=mydeck):
#    # Your code here.
#    shuffle(deck)
#    d = []
#    for i in range(numhands):
#        hand = []
#        for j in range(n):
#            hand.append(deck[i*n+j])
#        d.append(hand)
#    return d

# deal from Norvig
def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

print deal(3)
