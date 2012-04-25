#!/usr/bin/env python

import random, itertools

def shuffle_teacher(deck):
	n = len(deck)
	swapped = [False]*n
	while False in swapped:
		i, j = random.randrange(n), random.randrange(n)
		swapped[i] = swapped[j] = True
		deck[i],deck[j] = deck[j],deck[i]
	return deck

def factorial(n):
	if n < 2: return 1
	return n * factorial(n-1)

n = 2
m = factorial(n)
while True:
	deck = [str(i) for i in range(1,n+1)]
	shuffle_teacher(deck)
	print '_'.join(deck)




	
