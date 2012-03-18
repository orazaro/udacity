#!/usr/bin/python
import urllib
import sys

def get_page(url):
    try:
        f = urllib.urlopen(url)
        s = f.read()
        f.close()
    except IOError, e:
        return ""
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

def union(p, q):
    for e in q:
        if e not in p:
            p.append(e)
    return p

def crawl_web(seed, max_depth):
    tocrawl = [[seed,0]]
    crawled = []
    while tocrawl:
        link, depth = tocrawl.pop()
        if link[:5] != 'http:':
            continue
        if depth <= max_depth and link not in crawled:
            crawled.append(link)
            print link
            if depth == max_depth:
                continue
            links = get_all_links(get_page(link))
            for e in links:
                if e not in crawled:
                    tocrawl.append([e,depth+1])
    return crawled

seed = "http://udacity.com/cs101x/index.html"
max_depth = 3
if len(sys.argv) > 1:
    seed = sys.argv[1]
if len(sys.argv) > 2:
    max_depth = int(sys.argv[2])
crawled = crawl_web(seed, max_depth)
print "crawled: ", len(crawled)



