#!/usr/bin/python
import urllib

def get_page(url):
    f = urllib.urlopen(url)
    s = f.read()
    f.close()
    return s

def get_next_url(page):
    href_pos = page.find('<a href=')
    if(href_pos == -1):
        return [None,0]
    first_pos = page.find('"', href_pos) + 1
    end_pos = page.find('"', first_pos)
    url = page[first_pos:end_pos]
    return [url,end_pos]

def print_all_urls(page):
    while True:
        [url, end_pos] = get_next_url(page)
        if url:
            print url
        else:
            break
        page = page[end_pos:]

def get_all_urls(page):
    urls = []
    while True:
        [url, end_pos] = get_next_url(page)
        if url:
            urls.append(url)
        else:
            break
        page = page[end_pos:]
    return urls


page = get_page("http://udacity.com/cs101x/index.html")
print page
print "=" * 20
print_all_urls(page)
print "=" * 20
urls = get_all_urls(page)
print urls

