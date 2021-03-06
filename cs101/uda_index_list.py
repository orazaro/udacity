#!/usr/bin/python

def add_to_index(index,keyword,url):
    """
    >>> index = []
    >>> add_to_index(index,'udacity','http://udacity.com')
    >>> add_to_index(index,'computing','http://acm.org')
    >>> add_to_index(index,'udacity','http://npr.org')
    >>> print index
    [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]
    """
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def lookup(index, keyword):
    """
    >>> index = [['one',[1]],['two',[2,22]],['three',[3,33,333]]]
    >>> print lookup(index, 'two')
    [2, 22]
    """
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return []

def add_page_to_index(index, url, content):
    """
    >>> index = []
    >>> add_page_to_index(index,'fake.text',"This is a test")
    >>> print index
    [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]
    """
    for keyword in content.split():
        add_to_index(index,  keyword, url)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
