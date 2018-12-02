#/usr/bin/env python3

from collections import Counter
from itertools import combinations

def p1(IDs):
    two_letters = 0
    three_letters = 0
    for i in IDs:
        letters = Counter(i)
        if 2 in letters.values():
            two_letters += 1
        if 3 in letters.values():
            three_letters += 1
    return two_letters * three_letters

def compare(id1, id2):
    """return a tuple (Bool, int) to say if the 2 strings differ only by one letter and at which position"""
    diff = -1
    for pos,l in enumerate(id1):
        if l != id2[pos]:
            if diff == -1:
                diff = pos
            else:
                return (False,0)
    return (True,diff)


def p2(IDs):
    for (id1, id2) in combinations(IDs, 2):
        (differ_1_letter, diff_position) = compare(id1,id2)
        if differ_1_letter:
            return id1[:diff_position] + id1[diff_position+1:]

if __name__ == "__main__":
    f = open('input.txt', 'r')
    IDs = [x.rstrip() for x in f.readlines()]
    print("part1: {}".format(p1(IDs)))
    print("part2: {}".format(p2(IDs)))
