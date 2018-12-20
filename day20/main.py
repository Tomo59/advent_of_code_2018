#!/usr/bin/env python3

import sys

def move(y, x, cur_weight, regex, cur_rooms, saved_positions):
    cur_rooms.append(((y,x),cur_weight))
    c = regex.pop(0)
    if c == '$':
        return cur_rooms
    if c == 'N':
        return move(y-1, x, cur_weight+1, regex, cur_rooms, saved_positions)
    if c == 'S':                                 
        return move(y+1, x, cur_weight+1, regex, cur_rooms, saved_positions)
    if c == 'W':                                 
        return move(y, x-1, cur_weight+1, regex, cur_rooms, saved_positions)
    if c == 'E':                                 
        return move(y, x+1, cur_weight+1, regex, cur_rooms, saved_positions)
    if c == '(':
        saved_positions.append((y, x, cur_weight))
        return move(y, x, cur_weight, regex, cur_rooms, saved_positions)
    if c == '|':
        return move(*saved_positions[-1], regex, cur_rooms, saved_positions)
    if c == ')':
        return move(*saved_positions.pop(), regex, cur_rooms, saved_positions)
    raise ExceptionError("Should not be here, c is {}".format(c))


def p1(rooms_short):
    return max(rooms_short.values())


def p2(rooms_short):
    return len([x for x in rooms_short.values() if x >= 1000])

if __name__ == "__main__":
    f = open('input.txt', 'r')
    sys.setrecursionlimit(150000)
    regex = list(f.readline().rstrip())
    regex.pop(0) # remove '^'
    rooms = move(0, 0, 0, regex, [], [])
    rooms_short = dict()
    for k,v in rooms:
        if rooms_short.get(k,10000000) > v:
            rooms_short[k] = v
    print(rooms_short)
    print("part1: {}".format(p1(rooms_short)))
    print("part1: {}".format(p2(rooms_short)))

