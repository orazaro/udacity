#!/usr/bin/python

def poker(hands):
    "Return a list of winning hands: poker([hand,...]) => [hand,...]"
    return allmax(hands, key=hand_rank)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    # Your code here.
    result, keymax = [], None
    key = key or (lambda x: x)
    for e in iterable:
        k = key(e)
        if not result or keymax < k:
            result, keymax  = [e], k
        elif keymax == k:
            result.append(e)
    return result
            

def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
#    if ranks == [14,5,4,3,2]:
#        ranks = [5,4,3,2,1]
#    return ranks
    return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    # Your code here.
    for i in range(1,len(ranks)):
        if ranks[i-1] != ranks[i] + 1:
            return False
    return True
    
def flush(hand):
    "Return True if all the cards have the same suit."
    # Your code here.
#    color = ''
#    for r,c in hand:
#        if color and color != c:
#            return False
#        else:
#            color = c
#    return True
    suits = [s for r,s in hand]
    return len(set(suits)) == 1

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    pair = []
    for r in ranks:
        if ranks.count(r) == 2:
            if r not in pair: pair.append(r)
    if len(pair) != 2: return None
    if pair[0] > pair[1]: return (pair[0], pair[1])
    return (pair[1], pair[0])

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None

 
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    sf1 = "6C 7C 8C 9C TC".split() # Straight Flush
    sf2 = "6D 7D 8D 9D TD".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "TD TC 7H 7C KD".split() # Two Pairs
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert poker([sf, fk, fh]) == [sf]
    assert poker([fk, fh]) == [fk]
    assert poker([fh, fh]) == [fh,fh]
    assert poker([sf]) == [sf]
    assert poker([sf] + 99*[fh]) == [sf]
    assert poker([sf1, sf2, fk, fh]) == [sf1, sf2] 
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    assert straight(card_ranks(al)) == True

    return 'tests pass'

print test()

