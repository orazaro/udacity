#!/usr/bin/python

def mystery(p):
    i = 0;
    while True:
        if i >= len(p):
            break
        if p[i] % 2:
            i = i + 2
        else:
            i = i + 1
    return i

n = 100
for i in range(n):
    p.append(random.randint(1,n))


