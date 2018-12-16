#!/usr/bin/env python3

from enum import Enum, auto
import re

class OpCode(Enum):
    addr = auto()
    addi = auto()
    mulr = auto()
    muli = auto()
    banr = auto()
    bani = auto()
    borr = auto()
    bori = auto()
    setr = auto()
    seti = auto()
    gtir = auto()
    gtri = auto()
    gtrr = auto()
    eqir = auto()
    eqri = auto()
    eqrr = auto()

opcode_dict = {}

def execute(regs, opcode, A, B, C):
    """ return (key,value) the key of the regs to update with the corresponding value"""
    if opcode == OpCode.addr:
        return (C, regs.get(A, 0) + regs.get(B, 0))
    elif opcode == OpCode.addi:
        return (C, regs.get(A, 0) + B)
    elif opcode == OpCode.mulr:
        return (C, regs.get(A, 0) * regs.get(B, 0))
    elif opcode == OpCode.muli:
        return (C, regs.get(A, 0) * B)
    elif opcode == OpCode.banr:
        return (C, regs.get(A, 0) & regs.get(B, 0))
    elif opcode == OpCode.bani:
        return (C, regs.get(A, 0) & B)
    elif opcode == OpCode.borr:
        return (C, regs.get(A, 0) | regs.get(B, 0))
    elif opcode == OpCode.bori:
        return (C, regs.get(A, 0) | B)
    elif opcode == OpCode.setr:
        return (C, regs.get(A, 0))
    elif opcode == OpCode.seti:
        return (C, A)
    elif opcode == OpCode.gtir:
        if A > regs.get(B, 0):
            return (C, 1)
        else:
            return (C, 0)
    elif opcode == OpCode.gtri:
        if regs.get(A, 0) > B:
            return (C, 1)
        else:
            return (C, 0)
    elif opcode == OpCode.gtrr:
        if regs.get(A, 0) > regs.get(B, 0):
            return (C, 1)
        else:
            return (C, 0)
    elif opcode == OpCode.eqir:
        if A == regs.get(B, 0):
            return (C, 1)
        else:
            return (C, 0)
    elif opcode == OpCode.eqri:
        if regs.get(A, 0) == B:
            return (C, 1)
        else:
            return (C, 0)
    elif opcode == OpCode.eqrr:
        if regs.get(A, 0) == regs.get(B, 0):
            return (C, 1)
        else:
            return (C, 0)

def p1(samples):
    result = 0
    for (sample_input, op, sample_after) in samples:
        regs = dict()
        for r,s in enumerate(sample_input):
            regs[r] = s
        opcodes_matched = set()
        for o in OpCode:
            (k,v) = execute(regs, o, op[1], op[2], op[3])
            if k < 4:
                sample_input[k] = v
                if sample_input == sample_after:
                    opcodes_matched.add(o)
        if len(opcodes_matched) >= 3:
            result += 1
        # filter all known operations to see if we can know what is op[0]
        opcodes_matched -= set(opcode_dict.values())
        if len(opcodes_matched) == 1:
            opcode_dict[op[0]] = opcodes_matched.pop()
    #print(opcode_dict)
    return result

def p2(program):
    regs = dict()
    for op in program:
        (k,v) = execute(regs, opcode_dict[op[0]], op[1], op[2], op[3])
        regs[k] = v
    return regs[0]

if __name__ == "__main__":
    f = open('input.txt', 'r')
    samples = []
    line = f.readline().rstrip()
    while len(line):
        sample_before = list(map(int, re.findall(r"[\d']+", line)))
        line = f.readline().rstrip()
        op = list(map(int, re.findall(r"[\d']+", line)))
        line = f.readline().rstrip()
        sample_after = list(map(int, re.findall(r"[\d']+", line)))
        samples.append((sample_before, op, sample_after))
        line = f.readline().rstrip()
        line = f.readline().rstrip()
    f.readline()
    program = [list(map(int, re.findall(r"[\d']+", line))) for line in f.readlines()]
    print("part1: {}".format(p1(samples)))
    print("part2: {}".format(p2(program)))

