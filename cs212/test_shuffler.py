#!/usr/bin/env python
# test shufflers from Norvig
import random, itertools
from collections import defaultdict

def shuffle(deck):
	n = len(deck)
	for i in range(n):
		j = random.randrange(n-i)
		deck[i],deck[j] = deck[j],deck[i]
	return deck

def shuffle1(deck):
	n = len(deck)
	swapped = [False]*n
	while False in swapped:
		i, j = random.randrange(n), random.randrange(n)
		swapped[i] = swapped[j] = True
		deck[i],deck[j] = deck[j],deck[i]
	return deck

def test_shuffler(shuffler, deck='abcd', n=10000):
	counts = defaultdict(int)
	for _ in range(n):
		input = list(deck)
		shuffler(input)
		counts[''.join(input)] += 1
	e = n*1./factorial(len(deck))	## expected count
	ok = all((0.9 <= counts[item]/e <= 1.1)
			for item in counts)
	name = shuffler.__name__
	print '%s(%s) %s' % (name, deck, ('ok' if ok else '*** BAD ***'))
	print '   ',
	for item, count in sorted(counts.items()):
		print "%s:%4.1f" % (item, count*100./n),
	print

def test_shufflers(shufflers=[shuffle, shuffle1], decks=['abc','ab']):
	for deck in decks:
		print
		for f in shufflers:
			test_shuffler(f, deck)

def factorial(n): return 1 if (n <= 1) else n*factorial(n-1)

test_shufflers()
