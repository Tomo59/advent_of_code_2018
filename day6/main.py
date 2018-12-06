#/usr/bin/env python3

from collections import Counter

def manhattan(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def p1(points):
    x_min = min(points, key=lambda p: p[0])[0]
    x_max = max(points, key=lambda p: p[0])[0]
    y_min = min(points, key=lambda p: p[1])[1]
    y_max = max(points, key=lambda p: p[1])[1]
    grid = {}
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            grid[(x,y)] = sorted(enumerate(points), key=lambda p: manhattan(p[1], (x,y)))
            if manhattan(grid[(x,y)][0][1], (x,y)) == manhattan(grid[(x,y)][1][1], (x,y)):
                grid[(x,y)] = -1
            else:
                grid[(x,y)] = grid[(x,y)][0][0]
    return max(Counter(grid.values()).values())

def p2(points):
    x_min = min(points, key=lambda p: p[0])[0]
    x_max = max(points, key=lambda p: p[0])[0]
    y_min = min(points, key=lambda p: p[1])[1]
    y_max = max(points, key=lambda p: p[1])[1]
    result = 0
    for x in range(x_min, x_max+1):
        for y in range(y_min, y_max+1):
            if sum([manhattan(p, (x,y)) for p in points]) < 10000:
                result += 1
    return result

if __name__ == "__main__":
    f = open('input.txt', 'r')
    points = [[int(x) for x in l.rstrip().split(', ')] for l in f.readlines()]
    print("part1: {}".format(p1(points)))
    print("part2: {}".format(p2(points)))
