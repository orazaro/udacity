import random
import string
import hashlib

def make_salt():
    return ''.join(random.choice(string.letters) for x in xrange(5))

def make_pw_hash(name, pw, salt = None):
    if not salt: 
        salt = make_salt()
    h = hashlib.sha256(name + pw + salt).hexdigest()
    return '%s,%s' % (h, salt)

def valid_pw(name, pw, h):
    salt = h.split(',')[-1]
    return h == make_pw_hash(name, pw, salt) 

if __name__ == '__main__':
    h = make_pw_hash('spez', 'hunter2')
    print h
    print valid_pw('spez', 'hunter2', h)

