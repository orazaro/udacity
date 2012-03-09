#!/usr/bin/python
import urllib, sys

def get_page(url):
    try:
        f = urllib.urlopen(url)
        s = f.read()
        f.close()
    except:
        return ''
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
    #print "hrefend=",hrefend, " : ", page[hrefend:hrefend+10]
    if(hrefend == -1):
        return [None,0]
    firstpos = page.find('"', hrefend) + 1
    endpos = page.find('"', firstpos)
    url = page[firstpos:endpos]
    if url:
        return url, endpos
    else:
        return get_next_url(page[endpos:])

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

#seed = "http://udacity.com/cs101x/index.html"
seed = "http://rambler.ru/"
page = get_page(seed)
print page
print "=" * 20

tocrawl = [seed]
crawled = []
while(len(tocrawl)):
    url = tocrawl.pop()
    print url
    links = get_all_links(get_page(url))
    crawled.append(url)
    print links
    for e in links:
        if e not in crawled:
            tocrawl.append(e)
    print "*" * 70


