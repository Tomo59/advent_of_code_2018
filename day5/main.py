#/usr/bin/env python3

import string

def react(a, b):
    """giving 2 char a and b say is they react (a is the capitalized b or vice versa)"""
    return a!=b and a.lower()==b.lower()

def p1(polymer):
    """ make all the polymer react """
    p = list(polymer)
    i = 0
    while i < len(p)-1:
        if react(p[i], p[i+1]):
            del p[i]
            del p[i]
            i -= 2
        i += 1
    return len(p)

def p2(polymer):
    return min([p1(polymer.replace(x, "").replace(x.lower(), "")) for x in string.ascii_uppercase])

if __name__ == "__main__":
    f = open('input.txt', 'r')
    polymer = f.readline().rstrip()
    print("part1: {}".format(p1(polymer)))
    print("part2: {}".format(p2(polymer)))
