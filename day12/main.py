#/usr/bin/env python3

from collections import Counter

def p1(initial_state, combis, nb_round):
    #first extend the list to the left and right (maximum 20*2 on each side)
    states = [False]*nb_round*2 + initial_state + [False]*nb_round*2
    states_len = len(states)
    for i in range(nb_round):
        new_states = [False, False]
        for x in range(states_len-4):
            new_states.append(combis[(states[x], states[x+1], states[x+2], states[x+3], states[x+4])])
        new_states.extend([False, False])
        states = new_states
    result = 0
    for x in range(-2*nb_round, states_len-2*nb_round):
        if states[x+2*nb_round]:
            result += x
    return result

def normalize(states):
    """ modify the dict so that it starts and ends with true and first key is 0"""
    l = []
    for k,v in states.items():
        if v:
            l.append(k)
    k_min = min(l)
    k_max = max(l)
    new_states = {}
    for k in range(0, k_max-k_min+1):
        new_states[k] = states[k+k_min]
    return (new_states, k_min)
    
def beautiful(s):
    result = ""
    for k in sorted(s.keys()):
        if s[k]:
            result += '#'
        else:
            result += '.'
    return result

def p2(initial_state, combis, nb_round):
    #p2 is the same as p1 but faster
    states = {}
    for i,s in enumerate(initial_state):
        states[i] = s
    states_list = []
    shift_list = []
    loop = 0
    shift = 0
    new_shift = 0
    while states not in states_list and loop < nb_round:
        states_list.append(states)
        shift_list.append(new_shift)
        new_states = {}
        for x in states.keys():
            new_states[x] = combis[(states.get(x-2, False),
                                    states.get(x-1, False),
                                    states.get(x  , False),
                                    states.get(x+1, False),
                                    states.get(x+2, False))]
        x = min(states.keys()) - 1
        if combis[(states.get(x-2, False),
                   states.get(x-1, False),
                   states.get(x  , False),
                   states.get(x+1, False),
                   states.get(x+2, False))]:
            new_states[x] = True
        x = max(states.keys()) + 1
        if combis[(states.get(x-2, False),
                   states.get(x-1, False),
                   states.get(x  , False),
                   states.get(x+1, False),
                   states.get(x+2, False))]:
            new_states[x] = True
        (states, new_shift) = normalize(new_states)
        shift += new_shift
        loop += 1

    if loop == nb_round:
        result = 0
        for k in states.keys():
            if states[k]:
                result += k + shift
        return result

    loop_start = states_list.index(states)
    loop_end = len(states_list)
    #print("found a loop from  {} to {} round".format(loop_start, loop_end))
    #for s in states_list:
    #    print(beautiful(s))
    #print(beautiful(states))
    todo = nb_round - loop_start - 1
    loop_size = loop_end - loop_start
    if loop_size * (todo//loop_size) == todo:
        # todo is a multiple of loop_size
        result = 0
        for k in states.keys():
            if states[k]:
                result += k + shift
        return result + (Counter(states.values())[True])*(todo//loop_size)*sum(shift_list[loop_start:loop_end])
        
    return "didn't solve it"

if __name__ == "__main__":
    f = open('input.txt', 'r')
    initial_state = [x == '#' for x in f.readline()[15:]]
    f.readline() # read empty line
    combis = {}
    for l in f.readlines():
        combis[(l[0] == '#', l[1] == '#', l[2] == '#', l[3] == '#', l[4] == '#')] = l[9] == '#'
    print("part1: {}".format(p1(initial_state, combis, 20)))
    print("part1 (with p2): {}".format(p2(initial_state, combis, 20)))
    print("part2: {}".format(p2(initial_state, combis, 50000000000)))
