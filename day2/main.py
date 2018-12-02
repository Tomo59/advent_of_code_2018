#/usr/bin/env python3

from collections import Counter

def p1(IDs):
    two_letters = 0
    three_letters = 0
    for i in IDs:
        letters = Counter(list(i))
        if 2 in letters.values():
            two_letters = two_letters + 1
        if 3 in letters.values():
            three_letters = three_letters + 1
    return two_letters * three_letters

def compare(id1, id2):
    """return a tuple (Bool, int) to say if the 2 strings differ only by one letter and at which position"""
    diff = -1
    for pos,l in enumerate(list(id1)):
        if l != list(id2)[pos]:
            if diff == -1:
                diff = pos
            else:
                return (False,0)
    return (True,diff)


def p2(IDs):
    for pos,i in enumerate(IDs):
        for j in IDs[pos+1:]:
            (differ_1_letter, diff_position) = compare(i,j)
            if differ_1_letter:
                l = list(j)
                del l[diff_position]
                return "".join(l)

if __name__ == "__main__":
    f = open('input.txt', 'r')
    IDs = [x.rstrip() for x in f.readlines()]
    print("part1: {}".format(p1(IDs)))
    print("part2: {}".format(p2(IDs)))
