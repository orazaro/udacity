#!/usr/bin/python
import urllib

def get_page(url):
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    return s

def get_next_url(page):
    href = page.find('<a href=')
    if(href == -1):
        return [None,0]
    firstpos = page.find('"', href) + 1
    endpos = page.find('"', firstpos)
    url = page[firstpos:endpos]
    return url, endpos

def print_all_urls(page):
    while True:
        url, end_pos = get_next_url(page)
        if url:
            print url
            page = page[end_pos:]
        else:
            return

def get_all_urls(page):
    urls = []
    while True:
        url, end_pos = get_next_url(page)
        if url:
            urls.append(url)
            page = page[end_pos:]
        else:
            break
    return urls


page = get_page("http://udacity.com/cs101x/index.html")
print page
print "=" * 20
print_all_urls(page)
print "=" * 20
urls = get_all_urls(page)
print urls

