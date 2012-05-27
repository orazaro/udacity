# -----------------
# User Instructions
# 
# Add a few new test cases to begin familiarizing yourself 
# with doctest. 


import doctest

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    # your code here
    d = {}
    if C1>M1>0 or C2>M2>0:
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



def mc_problem(start=(3,3,1,0,0,0), goal=None):
    "Find the fastest (least elapsed time) path to the goal in the bridge problem."
    if goal is None: 
        goal = (0,0,0) + start[:3]
    if start == goal:
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        state1 = path[-1]
        #print path 
        if state1 == goal:  ## Check for solution when we pull best path off frontier
            return path
        for (state, action) in csuccessors(state1).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                # Don't check for solution when we extend a path
                add_to_frontier(frontier,path2)
                frontier.sort(key=lambda path:len(path))
                #print 'front:', frontier
    return Fail

Fail = ()

def add_to_frontier(frontier, path):
    old = None
    for i,p in enumerate(frontier):
        if p[-1] == path[-1]:
            old = i
            break
    if old is not None and len(frontier[i]) <= len(path):
        return
    elif old is not None:
        del frontier[old]
    frontier.append(path)

class TestBridge: """
    >>> mc_problem((3,3,1,0,0,0),(0,0,0,3,3,1))
    [(3, 3, 1, 0, 0, 0), 'CC->', (3, 1, 0, 0, 2, 1), '<-C', (3, 2, 1, 0, 1, 0), 'CC->', (3, 0, 0, 0, 3, 1), '<-C', (3, 1, 1, 0, 2, 0), 'MM->', (1, 1, 0, 2, 2, 1), '<-MC', (2, 2, 1, 1, 1, 0), 'MM->', (0, 2, 0, 3, 1, 1), '<-C', (0, 3, 1, 3, 0, 0), 'CC->', (0, 1, 0, 3, 2, 1), '<-M', (1, 1, 1, 2, 2, 0), 'MC->', (0, 0, 0, 3, 3, 1)]

"""

print doctest.testmod()
print mc_problem((3,3,1,0,0,0),(0,0,0,3,3,1))
print mc_problem((6,5,1,0,0,0),(0,0,0,6,5,1))
#print mc_problem()
