#!/usr/bin/env python3



def adjacent(y,x,units,table):
    result = []
    units_pos = [(u[0],u[1]) for u in units]
    if table[y-1][x] and (y-1,x) not in units_pos:
        result.append((y-1,x))
    if table[y][x-1] and (y,x-1) not in units_pos:
        result.append((y,x-1))
    if table[y][x+1] and (y,x+1) not in units_pos:
        result.append((y,x+1))
    if table[y+1][x] and (y+1,x) not in units_pos:
        result.append((y+1,x))
    return result

def try_pos(y, x, begin_y, begin_x, target_y, target_x, table, pos, visited):
    if not table[y][x]:
        return False
    if (y,x) in visited:
        return False
    if y == target_y and x == target_x:
        return True
    pos.append((y, x, begin_y, begin_x))
    visited.add((y,x))
    return False

def next_move_for_target(y, x, units, target_y, target_x, table):
    pos = []
    visited = set((y,x))
    for p in adjacent(y,x,units,table):
        if try_pos(*p, *p, target_y, target_x, table, pos, visited):
            return p
    while len(pos):
        cur_pos = pos.pop(0)
        for p in adjacent(cur_pos[0], cur_pos[1], units, table):
            if try_pos(*p, cur_pos[2], cur_pos[3], target_y, target_x, table, pos, visited):
                return (cur_pos[2],cur_pos[3])
    raise(ExceptionError("didn't find a path"))

def give_good_targets(y, x, units, targets, table):
    pos = [(y,x)]
    visited = set((y,x))
    weight = 0
    result = []
    while len(pos):
        new_pos = []
        while len(pos):
            cur_pos = pos.pop(0)
            for p in adjacent(cur_pos[0], cur_pos[1], units, table):
                (y,x)=p
                if (y,x) in targets:
                    result.append((weight, y, x))
                elif table[y][x] and (y,x) not in visited:
                    new_pos.append((y,x))
                    visited.add((y,x))
        # as soon as we have some targets for a given weight, no need to try heavier targets
        if len(result):
            return result
        weight += 1
        pos = new_pos
    return result

def move(y, x, is_elf, hit, units, table):
    targets = set()
    for u in units:
        if u[2] != is_elf:
            targets.update(adjacent(u[0],u[1],units,table))
    #print(targets)
    if len(targets) == 0:
      return (y, x, is_elf, hit)
    if (y,x) in targets:
      return (y, x, is_elf, hit)
    # filter targets to keep only the shortest path 
    #print("trying to move from ({},{}). List of targets:".format(y,x))
    #print(targets)
    good_targets = give_good_targets(y, x, units, targets, table)
    #print(good_targets)
    if not good_targets:
        return (y, x, is_elf, hit)
    target = sorted(good_targets)[0]
    (new_y,new_x) = next_move_for_target(y, x, units, target[1], target[2], table)
    #print("have moved to ({},{})".format(new_y, new_x))
    return (new_y, new_x, is_elf, hit)

def attack(y, x, is_elf, hit, units, new_units, table, elf_attack):
    targets = [(u[0],u[1]) for u in units+new_units if u[2] != is_elf]
    units_pos = [(u[0],u[1]) for u in units+new_units]
    if len(targets) == 0:
        return False
    available_attack = []
    if (y-1,x) in targets:
        p = units_pos.index((y-1,x))
        available_attack.append(((units+new_units)[p][3],0,p,y-1,x))
    if (y,x-1) in targets:
        p = units_pos.index((y,x-1))
        available_attack.append(((units+new_units)[p][3],1,p,y,x-1))
    if (y,x+1) in targets:
        p = units_pos.index((y,x+1))
        available_attack.append(((units+new_units)[p][3],2,p,y,x+1))
    if (y+1,x) in targets:
        p = units_pos.index((y+1,x))
        available_attack.append(((units+new_units)[p][3],3,p,y+1,x))
    if len(available_attack):
        available_attack.sort()
        #print("we can attack all the following {}".format(available_attack))
        p = available_attack[0][2]
        if p < len(units):
            #print("unit({},{}) attacks unit({},{}) which is now at {} points".format(y,x,units[p][0], units[p][1], units[p][3]-3))
            if is_elf:
                units[p] = (units[p][0], units[p][1], units[p][2], units[p][3] - elf_attack)
            else:
                units[p] = (units[p][0], units[p][1], units[p][2], units[p][3] - 3)
            if units[p][3] <= 0:
                del units[p]
        else:
            p -= len(units)
            #print("unit({},{}) attacks unit({},{}) which is now at {} points".format(y,x,new_units[p][0], new_units[p][1], new_units[p][3]-3))
            if is_elf:
                new_units[p] = (new_units[p][0], new_units[p][1], new_units[p][2], new_units[p][3] - elf_attack)
            else:
                new_units[p] = (new_units[p][0], new_units[p][1], new_units[p][2], new_units[p][3] - 3)
            if new_units[p][3] <= 0:
                del new_units[p]
    return True


def p1(table, units, elf_attack):
    rounds = 0
    units.sort()
    while True:
        new_units = []
        while len(units):
            cur_unit = move(*units.pop(0), units+new_units, table)
            new_units.append(cur_unit)
            if not attack(*cur_unit, units, new_units, table, elf_attack):
                units.extend(new_units)
                return (rounds * sum([u[3] for u in units]), units)
        units = new_units
        units.sort()
        rounds += 1
        #print("")
        #print("ROUND {}:".format(rounds))

def p2(table, units):
    total_nb_elf = len([u for u in units if u[2]])

    elf_attack = 4
    (r, end_units) = p1(table, list(units), elf_attack)
    print("with power attack of {} it remains {}/{} elves".format(elf_attack, len([u for u in end_units if u[2]]), total_nb_elf))
    while len([u for u in end_units if u[2]]) != total_nb_elf:
        elf_attack += 1
        (r, end_units) = p1(table, list(units), elf_attack)
        print("with power attack of {} it remains {}/{} elves".format(elf_attack, len([u for u in end_units if u[2]]), total_nb_elf))
    return r

if __name__ == "__main__":
    f = open('input.txt', 'r')
    table = dict()
    units = []
    for i,line in enumerate(f):
        table[i] = dict()
        for j,c in enumerate(list(line)[:-1]):
            if c == 'E' or c == 'G':
                units.append((i,j,c=='E',200))
                table[i][j] = True # True means we can move on this cell
            else:
                table[i][j] = c == '.'
    print("part1: {}".format(p1(table, list(units), 3)[0]))
    print("part2: {}".format(p2(table, units)))

