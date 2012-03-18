#!/usr/bin/python
import urllib
import sys

from uda_index import add_page_to_index

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

def crawl_web(seed, index, max_depth = 3):
    """
    >>> crawled,index = crawl_web('http://udacity.com/cs101x/index.html',[], 3)
    >>> print crawled[1]
    http://www.udacity.com/cs101x/flying.html
    >>> print len(crawled)
    6
    >>> print len(index)
    51
    """
    tocrawl = [[seed,0]]
    crawled = []
    while tocrawl:
        link, depth = tocrawl.pop()
        if link[:5] != 'http:':
            continue
        if depth == max_depth:
            continue
        if depth <= max_depth and link not in crawled:
            page = get_page(link)
            add_page_to_index(index, link, page)
            links = get_all_links(page)
            crawled.append(link)
            for link in links:
                if link not in crawled:
                    tocrawl.append([link, depth+1])
    return crawled, index


if __name__ == '__main__':
    if '--test' in sys.argv[1:]:
        import doctest
        ret = doctest.testmod()
        sys.exit(ret.failed)
    seed = "http://udacity.com/cs101x/index.html"
    max_depth = 3
    if len(sys.argv) > 1:
        seed = sys.argv[1]
    if len(sys.argv) > 2:
        max_depth = int(sys.argv[2])
    crawled,index = crawl_web(seed, [], max_depth)
    #print "crawled: ", crawled
    print "links: ", len(crawled)
    print "index:"
#    for item in web_index:
#        print item[0], ': ', item[1]
    print 'keywords: ', len(index)

