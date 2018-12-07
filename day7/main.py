#/usr/bin/env python3

import copy
import time

def remove_letter(n, requirements):
    for k in list(requirements.keys()):
        if len(requirements[k]) == 1 and requirements[k][0] == n:
            #print("letter {} is now available".format(k))
            del requirements[k]
        elif n in requirements[k]:
            requirements[k].remove(n)

def p1(letters, requirements):
    result = ""
    while letters:
        available = letters - requirements.keys()
        n = sorted(available, reverse=True).pop()
        result += n
        letters.remove(n)
        remove_letter(n, requirements)
    return result

def p2(letters, requirements):
    result = []
    timestamp = 0
    available_list = sorted(letters - requirements.keys(), reverse=True)
    while letters:
        while (len(result) and result[0][0] == timestamp) or \
              (len(result) < 5 and len(available_list)):
            
            # remove the letter if elf finished processing it
            if len(result) and result[0][0] == timestamp:
                letters.remove(result[0][1])
                #print("  REMOVING {}".format(result[0][1]))
                remove_letter(result.pop(0)[1], requirements)
                available_list = sorted(letters - requirements.keys() - set([x[1] for x in result]), reverse=True)
                #print("  CALCULATE AVAILABLE : timestamp = {}, available: {}".format(timestamp, available_list))

            # prepare the work for next elves
            if len(result) < 5 and len(available_list):
                n = available_list.pop()
                result.append((timestamp + ord(n) - 4, n)) # ord('A') = 65
                #print("  available_list : {}, preparing: {} (available in {} seconds), result is now {}".format(available_list, n, ord(n) - 4, result))

        if len(result):
            result.sort()
            timestamp = result[0][0]
            #print("")
            #print("CHANGING TIMESTAMP: {}".format(timestamp))
    return timestamp

if __name__ == "__main__":
    f = open('input.txt', 'r')
    requirements = dict()
    letters = set()
    for l in f.readlines():
        letters.add(l[5])
        letters.add(l[36])
        if l[36] not in requirements.keys():
            requirements[l[36]] = list()
        requirements[l[36]].append(l[5])
    print("part1: {}".format(p1(set(letters), copy.deepcopy(requirements))))
    print("part2: {}".format(p2(set(letters), requirements)))
