#/usr/bin/env python3

def p1(jumps):
    return sum(jumps)

def p2(jumps):
    s = set()
    f = 0
    while True:
        for j in jumps:
            f += j
            if f in s:
                return f
            s.add(f)

if __name__ == "__main__":
    f = open('input.txt', 'r')
    jumps = [int(x) for x in f.readlines()]
    print("part1: {}".format(p1(jumps)))
    print("part2: {}".format(p2(jumps)))
