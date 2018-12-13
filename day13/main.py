#!/usr/bin/env python3



from enum import IntEnum
class Dir(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Turn(IntEnum):
    LEFT = 0
    STRAIGHT = 1
    RIGHT = 2

def change_dir(direction, turn):
    if turn == Turn.LEFT:
        if direction == Dir.UP:
            return Dir.LEFT
        if direction == Dir.DOWN:
            return Dir.RIGHT
        if direction == Dir.RIGHT:
            return Dir.UP
        if direction == Dir.LEFT:
            return Dir.DOWN
    if turn == Turn.RIGHT:
        if direction == Dir.UP:
            return Dir.RIGHT
        if direction == Dir.DOWN:
            return Dir.LEFT
        if direction == Dir.RIGHT:
            return Dir.DOWN
        if direction == Dir.LEFT:
            return Dir.UP
    if turn == Turn.STRAIGHT:
        return direction
        

def move(y, x, direction, turn, table):
    #print("we are at position [{}][{}]".format(y, x))
    if direction == Dir.UP:
        if table[y-1][x] == '+':
            return y-1,x,change_dir(direction, turn), (turn+1)%3
        elif table[y-1][x] == '|':
            return y-1,x,Dir.UP,turn
        elif table[y-1][x] == '\\':
            return y-1,x,Dir.LEFT,turn
        elif table[y-1][x] == '/':
            return y-1,x,Dir.RIGHT,turn
    if direction == Dir.DOWN:
        if table[y+1][x] == '+':
            return y+1,x,change_dir(direction, turn), (turn+1)%3
        elif table[y+1][x] == '|':
            return y+1,x,Dir.DOWN,turn
        elif table[y+1][x] == '\\':
            return y+1,x,Dir.RIGHT,turn
        elif table[y+1][x] == '/':
            return y+1,x,Dir.LEFT,turn
    if direction == Dir.RIGHT:
        if table[y][x+1] == '+':
            return y,x+1,change_dir(direction, turn), (turn+1)%3
        elif table[y][x+1] == '-':
            return y,x+1,Dir.RIGHT,turn
        elif table[y][x+1] == '\\':
            return y,x+1,Dir.DOWN,turn
        elif table[y][x+1] == '/':
            return y,x+1,Dir.UP,turn
    if direction == Dir.LEFT:
        if table[y][x-1] == '+':
            return y,x-1,change_dir(direction, turn), (turn+1)%3
        elif table[y][x-1] == '-':
            return y,x-1,Dir.LEFT,turn
        elif table[y][x-1] == '\\':
            return y,x-1,Dir.UP,turn
        elif table[y][x-1] == '/':
            return y,x-1,Dir.DOWN,turn
    raise Exception('CANNOT MOVE {}, {}, {}'.format(y,x,direction))
    return

def p1(table, carts):
    len_carts = len(carts)
    while True:
        for i in range(len_carts):
            new_cart = move(*carts.pop(0), table)
            if (new_cart[0],new_cart[1]) in [(x[0],x[1]) for x in carts]:
                return "{},{}".format(new_cart[1],new_cart[0])
            carts.append(new_cart)
        carts.sort()

def p2(table, carts):
    while len(carts) > 1:
        new_carts = []
        while len(carts):
            new_cart = move(*carts.pop(0), table)
            if (new_cart[0],new_cart[1]) in [(x[0],x[1]) for x in new_carts]:
                del new_carts[[(x[0],x[1]) for x in new_carts].index((new_cart[0],new_cart[1]))]
            elif (new_cart[0],new_cart[1]) in [(x[0],x[1]) for x in carts]:
                del carts[[(x[0],x[1]) for x in carts].index((new_cart[0],new_cart[1]))]
            else:
                new_carts.append(new_cart)
        carts = new_carts
        carts.sort()
    return "{},{}".format(carts[0][1],carts[0][0])

if __name__ == "__main__":
    f = open('input.txt', 'r')
    table = dict()
    carts = []
    for i,line in enumerate(f):
        table[i] = dict()
        for j,d in enumerate(list(line)[:-1]):
            if d == '>':
                carts.append((i,j,Dir.RIGHT,Turn.LEFT))
                table[i][j] = '-'
            elif d == '<':
                carts.append((i,j,Dir.LEFT,Turn.LEFT))
                table[i][j] = '-'
            elif d == '^':
                carts.append((i,j,Dir.UP,Turn.LEFT))
                table[i][j] = '|'
            elif d == 'v':
                carts.append((i,j,Dir.DOWN,Turn.LEFT))
                table[i][j] = '|'
            else:
                table[i][j] = d
    print("part1: {}".format(p1(table, list(carts))))
    print("part2: {}".format(p2(table, carts)))

