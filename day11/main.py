#/usr/bin/env python3

import operator

def power_level(x, y, serial):
    power = ((x+10) * y) + serial
    power *= (x+10)
    power = (power//100) % 10
    power -= 5
    return power

def p1(grid):
    grid_sum = {}
    for x in range(1,298):
        for y in range(1,298):
            grid_sum[(x,y)] = grid[(x+0,y+0)] + grid[(x+1,y+0)] + grid[(x+2,y+0)] \
                            + grid[(x+0,y+1)] + grid[(x+1,y+1)] + grid[(x+2,y+1)] \
                            + grid[(x+0,y+2)] + grid[(x+1,y+2)] + grid[(x+2,y+2)]
    return "{},{}".format(*max(grid_sum.items(), key=operator.itemgetter(1))[0])

def p2(grid):
    grid_sum = {}
    for size in range(1,301):
        for x in range(1,301-size):
            for y in range(1,301-size):
                if size == 1:
                    grid_sum[(x,y,size)] = grid[(x,y)]
                elif size == 2:
                    grid_sum[(x,y,size)] = grid[(x,y)]+grid[(x+1,y)]+grid[(x,y+1)]+grid[(x+1,y+1)]
                else:
                    grid_sum[(x,y,size)] = grid_sum[(x+1,y+0,size-1)] \
                                         + grid_sum[(x+0,y+1,size-1)] \
                                         - grid_sum[(x+1,y+1,size-2)] \
                                         + grid[(x,y)] + grid[(x+size,y+size)]
    return "{},{},{}".format(*max(grid_sum.items(), key=operator.itemgetter(1))[0])

if __name__ == "__main__":
    serial = 2694
    grid = {}
    for x in range(1,301):
        for y in range(1,301):
            grid[(x,y)] = power_level(x, y, serial)
    print("part1: {}".format(p1(grid)))
    print("part2: {}".format(p2(grid)))
