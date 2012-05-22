import hashlib

def make_secure_val(s):
    def hash_str(s):
        return hashlib.md5(s).hexdigest()
    return "%s,%s" % (s, hash_str(s))

# -----------------
# User Instructions
# 
# Implement the function check_secure_val, which takes a string of the format 
# s,HASH
# and returns s if hash_str(s) == HASH, otherwise None 

def check_secure_val(h):
    s = h.split(',')[0]
    return s if h==make_secure_val(s) else None

h = make_secure_val('udacity')
print h, '=>', check_secure_val(h)


