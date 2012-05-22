import random
import string

# implement the function make_salt() that returns a string of 5 random
# letters use python's random module.
# Note: The string package might be useful here.

def make_salt():
    s,n = '',len(string.letters)-1
    for _ in range(5):
        s += string.letters[random.randint(0,n)]
    return s
    
print make_salt()
