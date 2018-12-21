#!/usr/bin/env python3

from enum import Enum, auto
from functools import reduce
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

def exec(program, reg_ip, reg0_value):
    regs = dict()
    regs[0] = reg0_value
    ip = 0
    program_length = len(program)
    while ip >= 0 and ip < program_length:
        regs[reg_ip] = ip
        (k,v) = execute(regs, *program[ip])
        regs[k] = v
        ip = regs[reg_ip]
        ip += 1
    return regs[0]



def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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
    reg_ip = list(map(int, re.findall(r"[\d']+", line)))[0]
    program = [(OpCode[line[:4]], *list(map(int, re.findall(r"[\d']+", line[5:])))) for line in f.readlines()]
    print(program)
    #print("part1: {}".format(exec(program, reg_ip, 0)))
    print("part1: {}".format(sum(factors(961))))
    print("part2: {}".format(sum(factors(10551361))))

