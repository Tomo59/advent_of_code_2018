#/usr/bin/env python3

import re
import operator
from collections import Counter

def p1(sleep):
    """ find the guard with most total minute asleep"""
    sleepy_guard = max(sleep.items(), key=operator.itemgetter(1))[0]
    return sleepy_guard * max(sleep[sleepy_guard][1].items(), key=operator.itemgetter(1))[0]

def p2(sleep):
    """ find the guard with the minute most asleep"""
    sleepy_guard = max(sleep.items(), key=lambda x: max(x[1][1].values()))[0]
    return sleepy_guard * max(sleep[sleepy_guard][1].items(), key=operator.itemgetter(1))[0]

if __name__ == "__main__":
    f = open('input.txt', 'r')
    records = [l[1:].rstrip().split('] ') for l in f.readlines()]
    records.sort()
    sleep = dict()
    for r in records:
        if "Guard" in r[1]:
            guard_id = int(re.findall(r"[\d']+", r[1])[0])
        elif "falls asleep" == r[1]:
            minute_falls_asleep = int(r[0].split(':')[1])
        elif "wakes up" == r[1]:
            minute_wakes_up = int(r[0].split(':')[1])
            if not sleep.get(guard_id, None):
                sleep[guard_id] = []
            sleep[guard_id].extend(list(range(minute_falls_asleep, minute_wakes_up)))
    for k in sleep:
        # create (total number minute asleep, counter for each minute) tuple
        sleep[k] = (len(sleep[k]), Counter(sleep[k]))
    print("part1: {}".format(p1(sleep)))
    print("part2: {}".format(p2(sleep)))
