# -----------------
# User Instructions
# 
# Write a function, subway, that takes lines as input (read more about
# the **lines notation in the instructor comments box below) and returns
# a dictionary of the form {station:{neighbor:line, ...}, ... } 
#
# For example, when calling subway(boston), one of the entries in the 
# resulting dictionary should be 'foresthills': {'backbay': 'orange'}. 
# This means that foresthills only has one neighbor ('backbay') and 
# that neighbor is on the orange line. Other stations have more neighbors:
# 'state', for example, has 4 neighbors.
#
# Once you've defined your subway function, you can define a ride and 
# longest_ride function. ride(here, there, system) takes as input 
# a starting station (here), a destination station (there), and a subway
# system and returns the shortest path.
#
# longest_ride(system) returns the longest possible ride in a given 
# subway system. 

# -------------
# Grading Notes
#
# The subway() function will not be tested directly, only ride() and 
# longest_ride() will be explicitly tested. If your code passes the 
# assert statements in test_ride(), it should be marked correct.

import doctest

def subway(**lines):
    """Define a subway map. Input is subway(linename='station1 station2...'...).
    Convert that and return a dict of the form: {station:{neighbor:line,...},...}
    >>> print [x+'->'+s+'.'+a for x,y in subway(**{'q':'b c d','w':'a c'}).items() for s,a in y]
    ['a->c.w', 'c->b.q', 'c->d.q', 'c->a.w', 'b->c.q', 'd->c.q']
    """
    ## your code here
    from collections import defaultdict
    d = defaultdict(list)
    for name,line in lines.items():
        stations = line.split()
        for i,s in enumerate(stations):
            if i > 0:
                d[s].append([stations[i-1],name])
            if i < len(stations)-1:
                d[s].append([stations[i+1],name])
    return d

boston = subway(
    blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
    green='lechmere science north haymarket government park copley kenmore newton riverside',
    red='alewife davis porter harvard central mit charles park downtown south umass mattapan')

def ride(here, there, system=boston):
    """Return a path on the subway system from here to there.
    >>> print ride('mit', 'government')
    ['mit', 'red', 'charles', 'red', 'park', 'green', 'government']
    """
    ## your code here
    def successors(state):
        if state not in system:
            return {}
        d = {}
        for s in system[state]:
            d[s[0]] = s[1]
        return d
    def is_goal(state):
        return state == there
    start = here
    return shortest_path_search(start, successors, is_goal)

def longest_ride(system):
    """"Return the longest possible 'shortest path' 
    ride between any two stops in the system."""
    ## your code here
    import itertools
    states = system.keys()
    max_len = 0
    max_path = []
    for x,y in itertools.permutations(states,2):
        path = ride(x,y,system)
        if len(path) > max_len:
            max_len = len(path)
            max_path = path
    return max_path

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_states(path):
    "Return a list of states in this path."
    return path[0::2]
    
def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]

def test_ride():
    assert ride('mit', 'government') == [
        'mit', 'red', 'charles', 'red', 'park', 'green', 'government']
    assert ride('mattapan', 'foresthills') == [
        'mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
        'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 'orange', 'foresthills']
    assert ride('newton', 'alewife') == [
        'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
        'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife']
    assert (path_states(longest_ride(boston)) == [
        'wonderland', 'revere', 'suffolk', 'airport', 'maverick', 'aquarium', 'state', 'downtown', 'park',
        'charles', 'mit', 'central', 'harvard', 'porter', 'davis', 'alewife'] or 
        path_states(longest_ride(boston)) == [
                'alewife', 'davis', 'porter', 'harvard', 'central', 'mit', 'charles', 
                'park', 'downtown', 'state', 'aquarium', 'maverick', 'airport', 'suffolk', 'revere', 'wonderland'])
    assert len(path_states(longest_ride(boston))) == 16
    return 'test_ride passes'

#print [x+'->'+s+'.'+a for x,y in subway(**{'q':'b c d','w':'a c'}).items() for s,a in y]
#print ride('mit', 'government')
doctest.testmod()

longest_ride(boston)

print test_ride()

