#!/usr/bin/python
import urllib

def get_page(url):
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    return s

def find_href(page):
    h = page.find('<a')
    if h > 0 :
        h = page.find('href=', h + 2)
        if h > 0:
            return h + 4
    return -1

def get_next_url(page):
    hrefend = find_href(page)
    if(hrefend == -1):
        return [None,0]
    firstpos = page.find('"', hrefend) + 1
    endpos = page.find('"', firstpos)
    url = page[firstpos:endpos]
    return url, endpos

def get_all_links(page):
    page.lower()
    links = []
    while True:
        url, end_pos = get_next_url(page)
        if url:
            links.append(url)
            page = page[end_pos:]
        else:
            break
    return links

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)
    return p

start_page = "http://udacity.com/cs101x/index.html"
start_page = "http://rambler.ru/"
page = get_page(start_page)
print page
print "=" * 20
www = get_all_links(page)
print www
print "=" * 20
while(len(www)):
    url = www.pop()
    print url
    union(www,get_all_links(url))


