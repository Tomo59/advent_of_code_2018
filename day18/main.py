#!/usr/bin/env python3

from collections import Counter

def new_state(table):
    new_table = dict()
    for (i,j) in table.keys():
        if table[(i,j)] == '.':
            sum_tree = 0
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    if table.get((y,x), '@') == '|':
                        sum_tree += 1
            if sum_tree >= 3:
                new_table[(i,j)] = '|'
            else:
                new_table[(i,j)] = '.'
        if table[(i,j)] == '|':
            sum_lumberyard = 0
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    if table.get((y,x), '@') == '#':
                        sum_lumberyard += 1
            if sum_lumberyard >= 3:
                new_table[(i,j)] = '#'
            else:
                new_table[(i,j)] = '|'
        if table[(i,j)] == '#':
            sum_lumberyard = 0
            sum_tree = 0
            for y in range(i-1,i+2):
                for x in range(j-1,j+2):
                    if table.get((y,x), '@') == '|':
                        sum_tree += 1
                    elif table.get((y,x), '@') == '#':
                        sum_lumberyard += 1
            if sum_tree >= 1 and sum_lumberyard >= 2:
                new_table[(i,j)] = '#'
            else:
                new_table[(i,j)] = '.'
    return new_table

def p1(table):
    for a in range(10):
        table = new_state(table)
    counter = Counter(table.values())
    print(counter)
    return counter['|'] * counter['#']

def p2(table):
    list_states = []
    a = 0
    while a < 1000000000:
        table = new_state(table)
        if table in list_states:
            loop_start = list_states.index(table)
            loop_size = a - loop_start
            print("found a loop after {} iterations: state {} is the same as {}. Loop_size is {}.".format(a, a, loop_start, loop_size))
            while a < 1000000000:
                a += loop_size
            a -= loop_size
            print("a is now {}.".format(a))
            list_states = []
        list_states.append(table)
        a += 1
    counter = Counter(table.values())
    print(counter)
    return counter['|'] * counter['#']

if __name__ == "__main__":
    f = open('input.txt', 'r')
    table = dict()
    for i,line in enumerate(f):
        for j,c in enumerate(line):
            table[(i,j)] = c
    print("part1: {}".format(p1(dict(table))))
    print("part2: {}".format(p2(table)))

