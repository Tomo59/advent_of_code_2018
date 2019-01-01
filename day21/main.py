#!/usr/bin/env python3


def p1():
    r1 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    #while r3 != r0:
    r1 = r3 | 65536;
    r3 = 4921097;
    while True: 
        r4 = r1 & 255;
        r3 = r3 + r4;
        r3 = r3 & 16777215;
        r3 = r3 * 65899;
        r3 = r3 & 16777215;
        if (r1 < 256):
            break
        r4 = 0;
        while True: 
            r5 = r4 + 1;
            r5 = r5 * 256;
            if (r5 > r1):
                break
            r4 = r4 + 1;
        r1 = r4;
    return r3

def p2():
    l = []
    r1 = 0
    r3 = 0
    r4 = 0
    r5 = 0
    while True:
        r1 = r3 | 65536;
        r3 = 4921097;
        while True: 
            r4 = r1 & 255;
            r3 = r3 + r4;
            r3 = r3 & 16777215;
            r3 = r3 * 65899;
            r3 = r3 & 16777215;
            if (r1 < 256):
                break
            r4 = 0;
            while True: 
                r5 = r4 + 1;
                r5 = r5 * 256;
                if (r5 > r1):
                    break
                r4 = r4 + 1;
            r1 = r4;
        if r3 in l:
            return l.pop()
        l.append(r3)

if __name__ == "__main__":
    print("part1: {}".format(p1()))
    print("part2: {}".format(p2()))

