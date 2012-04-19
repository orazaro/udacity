#!/usr/bin/python
# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks_my(cards):
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

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse=True)
    return ranks

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert card_ranks(['AC', '3D', '4S', 'KH']) == [14, 13, 4, 3]
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9,9,9,9,7]
    assert card_ranks(fh) == [10,10,10,7,7]

test()
print 'ok'

