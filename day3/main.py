#/usr/bin/env python3

import re
from collections import Counter

def go_through_claim(claim):
    for x in range(claim[1], claim[1]+claim[3]):
        for y in range(claim[2], claim[2]+claim[4]):
            yield((x,y))

def claim_is_alone(claim, table):
    for coord in go_through_claim(claim):
        if table[coord] != 1:
             return False
    return True

def p1(table):
    counts = Counter(table.values())
    del counts[1]
    return sum(counts.values())

def p2(claims, table):
    for claim in claims:
        if claim_is_alone(claim, table):
            return claim[0]

if __name__ == "__main__":
    f = open('input.txt', 'r')
    claims = [list(map(int, re.findall(r"[\d']+", l))) for l in f.readlines()]
    # create the table containing how many claims are on each inch square
    table = {}
    for claim in claims:
        for coord in go_through_claim(claim):
            table[coord] = table.get(coord,0) + 1
    print("part1: {}".format(p1(table)))
    print("part2: {}".format(p2(claims, table)))
