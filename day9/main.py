#/usr/bin/env python3

import re

def p1(nb_player, last_marble):
    cur_player = 0
    cur_marble = 0
    scores = {}
    marbles = [0]
    for m in range(1, last_marble+1):
        if m % 23:
            if cur_marble == len(marbles)-1:
                cur_marble = 1
            else:
                cur_marble += 2
            marbles.insert(cur_marble, m)
        else:
            cur_marble = (cur_marble-7) % len(marbles)
            scores[cur_player] = scores.get(cur_player, 0) + m + marbles.pop(cur_marble)
        cur_player = (cur_player+1) % nb_player
    return max(scores.values())

class DoubleNode:
    def __init__(self, data):
        self.val = data
        self.next = None
        self.prev = None

# p2 is the same than p1 but faster !
def p2(nb_player, last_marble):
    cur_player = 0
    scores = {}
    marbles = DoubleNode(0)
    marbles.next = marbles
    marbles.prev = marbles
    head = marbles
    for m in range(1, last_marble+1):
        if m % 23:
            # go to the right once
            marbles = marbles.next
            # insert new marble
            new_marble = DoubleNode(m)
            prev_neighbour = marbles.next
            marbles.next = new_marble
            new_marble.prev = marbles
            new_marble.next = prev_neighbour
            prev_neighbour.prev = new_marble
            marbles = new_marble
        else:
            # go to the left 7 times
            marbles = marbles.prev.prev.prev.prev.prev.prev.prev
            scores[cur_player] = scores.get(cur_player, 0) + m + marbles.val
            # remove item
            prev_neighbour = marbles.next
            marbles.prev.next = prev_neighbour
            prev_neighbour.prev = marbles.prev
            del marbles
            marbles = prev_neighbour
        cur_player = (cur_player+1) % nb_player
    return max(scores.values())

if __name__ == "__main__":
    f = open('input.txt', 'r')
    ints = re.findall(r"[\d']+", f.readline())
    nb_player = int(ints[0])
    nb_marble = int(ints[1])
    print("part1: {}".format(p1(nb_player, nb_marble)))
    print("part2: {}".format(p2(nb_player, nb_marble*100)))
