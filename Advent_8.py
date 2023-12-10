#!/usr/bin/env python3

filename = 'A_8.txt'
maps = {}
rLseq = []
rL = 0
location = 'AAA'
steps = 0


def rLsequence(r_l):
    r_l += 1
    l = len(rLseq)
    if r_l == l:
        r_l = 0
    return r_l

with open(filename) as f:
    for line in f:
        line = line.strip()
        if 'LRRLRRRLRRRLLRRLR' in line:
            rLseq = list(line)
        else:
            k = line[0:3]
            v = [line[7:10], line[12:15]]
            maps[k] = v

while location != 'ZZZ':
    place = maps[location]
    rOrL = rLseq[rL]
    if rOrL == 'R':
        location = place[1]
    if rOrL == 'L':
        location = place[0]
    rL = rLsequence(rL)
    steps += 1
    print(f'The number of steps to reach {location} is {steps}!')