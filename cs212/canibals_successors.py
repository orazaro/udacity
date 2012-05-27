# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    d = {}
    if C1>M1 or C2>M2:
        return d
    vars=[(0,1),(1,0),(1,1),(2,0),(0,2)]
    if B1 > 0:
        for x,y in vars:
            if M1>=x and C1>=y:
                action = 'M'*x+'C'*y+'->'
                d[(M1-x, C1-y, B1-1, M2+x, C2+y, B2+1)] = action
    else:
        for x,y in vars:
            if M2>=x and C2>=y:
                action = '<-'+'M'*x+'C'*y
                d[(M1+x, C1+y, B1+1, M2-x, C2-y, B2-1)] = action
    return d

def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}
    assert csuccessors((1, 1, 0, 4, 3, 1)) == {(1, 2, 1, 4, 2, 0): '<-C', 
                                               (2, 1, 1, 3, 3, 0): '<-M', 
                                               (3, 1, 1, 2, 3, 0): '<-MM', 
                                               (1, 3, 1, 4, 1, 0): '<-CC', 
                                               (2, 2, 1, 3, 2, 0): '<-MC'}
    assert csuccessors((1, 4, 1, 2, 2, 0)) == {}
    return 'tests pass'

print test()

