#!/usr/bin/python
# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    for i in range(len(ranks)):
        j = 'TJQKA'.find(ranks[i])
        if j != -1:
            ranks[i] = 10 + j;
        else:
            ranks[i] = int(ranks[i])
    ranks.sort(reverse=True)
    return ranks

def card_ranks2(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = [r for r,s in cards]
    ranks = ['--23456789TJQKA'.index(r) for r in ranks]
    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]
print card_ranks2(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]

