#!/usr/bin/env python
# Implement the function escape_html(s), which replaces:
# > with &gt;
# < with &lt;
# " with &quot;
# & with &amp;
# and returns the escaped string
# Note that your browser will probably automatically 
# render your escaped text as the corresponding symbols, 
# but the grading script will still correctly evaluate it.
# 

def escape_html(s):
    d = {'>':'&gt;','<':'&lt;','"':'&quot;','&':'&amp;'}
    esc = ''
    for c in s:
        esc += d.get(c,c)
    return esc

print '123&2"xxxxx<q>'
print escape_html('123&2"xxxxx<q>')

