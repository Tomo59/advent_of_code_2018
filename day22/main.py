#!/usr/bin/env python3

def erosion_level(Y, X, depth, table, target_Y, target_X):
    if (Y,X) == (0,0):
        geological_index = 0
    elif (Y,X) == (target_Y, target_X):
        geological_index = 0
    elif Y == 0:
        geological_index = X * 16807
    elif X == 0:
        geological_index = Y * 48271
    else:
        geological_index = table[(Y,X-1)] * table[(Y-1,X)]
    return (geological_index + depth) % 20183


def fill_type(depth, target_X, target_Y, region_type, size_X, size_Y):
    cur_X = 0
    cur_Y = 0
    cur_length = 0
    while cur_Y != min(size_X,size_Y) or cur_X != min(size_X,size_Y):
        region_type[(cur_Y,cur_X)] = erosion_level(cur_Y, cur_X, depth, region_type, target_Y, target_X)
        # move
        if cur_X == cur_length and cur_Y == cur_length:
            cur_length += 1
            cur_Y = 0
            cur_X = cur_length
        elif cur_X == cur_length and cur_Y == cur_length -1:
            cur_X = 0
            cur_Y = cur_length
        elif cur_X == cur_length:
            cur_Y += 1
        else:
            cur_X += 1
    # we know that X < Y
    while cur_Y != size_Y or cur_X != size_X:
        region_type[(cur_Y,cur_X)] = erosion_level(cur_Y, cur_X, depth, region_type, target_Y, target_X)
        # move
        if cur_X == cur_length:
            cur_Y +=1
            cur_X = 0
        else:
            cur_X += 1
    region_type[(cur_Y,cur_X)] = erosion_level(cur_Y, cur_X, depth, region_type, target_Y, target_X)

    for k,v in region_type.items():
        region_type[k] = v%3
    
    #for yy in range(size_Y):
    #    for xx in range(size_X):
    #        t = region_type[(yy,xx)]
    #        if t == 0:
    #            print('.', end='')
    #        elif t == 1:
    #            print('=', end='')
    #        else:
    #            print('|', end='')
    #    print("")

def p1(target_X, target_Y, region_type):
    result = 0
    for yy in range(target_Y+1):
        for xx in range(target_X+1):
            result += region_type[(yy,xx)]
    return result

# X, Y are coordinates of the map
# t is the time to be at X, Y
# tool is the current tool we hold
def visit(prev_X, prev_Y, X, Y, t, tool, todo, time, size_X, size_Y, region_type):
    if X < 0 or X > size_X or Y < 0 or Y > size_Y:
        return
    if tool == region_type[(Y,X)] or tool == region_type[(prev_Y, prev_X)]: # forbidden tool
        return
    if (Y,X,tool) not in time.keys() or t < time[(Y,X,tool)]:
        time[(Y,X,tool)] = t
        #print("time[({},{},{})] = {}".format(Y,X,tool,t))
        todo.append((Y,X,tool))
    return

# neither 0
# torch 1
# climbing gear 2
def p2(X, Y, region_type):
    todo = [(0,0,1)]
    time = dict()
    time[(0,0,1)] = 0
    while len(todo):
        (cur_Y,cur_X,tool) = todo.pop(0)
        t = time[(cur_Y,cur_X,tool)]
        visit(cur_X, cur_Y, cur_X+1, cur_Y, t+1, (tool+0)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X+1, cur_Y, t+8, (tool+1)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X+1, cur_Y, t+8, (tool+2)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X-1, cur_Y, t+1, (tool+0)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X-1, cur_Y, t+8, (tool+1)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X-1, cur_Y, t+8, (tool+2)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X, cur_Y+1, t+1, (tool+0)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X, cur_Y+1, t+8, (tool+1)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X, cur_Y+1, t+8, (tool+2)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X, cur_Y-1, t+1, (tool+0)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X, cur_Y-1, t+8, (tool+1)%3, todo, time, X*2, Y*2, region_type)
        visit(cur_X, cur_Y, cur_X, cur_Y-1, t+8, (tool+2)%3, todo, time, X*2, Y*2, region_type)

    return time[(Y,X,1)]


if __name__ == "__main__":
    region_type = dict()
    (depth,X,Y) = (510,10,10) # example
    (depth,X,Y) = (3558,15,740) # my inpu
    fill_type(depth, X, Y, region_type, X*2, Y*2)
    print("part1: {}".format(p1(X, Y, region_type)))
    print("part2: {}".format(p2(X, Y, region_type)))

