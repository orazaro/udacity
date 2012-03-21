#!/usr/bin/python
import urllib

def get_page(url):
    try:
        return urllib.urlopen(url).read()
    except IOError, e:
        return ""

def test_hash_function(func, keys, size):
    result = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            h = func(w,size)
            result[h] += 1
            keys_used.append(w)
    return result
        
def hash_string(string, buckets):
    h = 0
    for c in string:
        h += ord(c)
    return h % buckets

words = get_page('http://www.gutenberg.org/cache/epub/1661/pg1661.txt').split()
result = test_hash_function(hash_string, words, 16)
print result

