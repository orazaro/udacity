#!/usr/bin/python

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword, len(htable))]


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

