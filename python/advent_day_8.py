from numpy import argmax


def format_input(file):
    statements = []
    registers = {}
    with open(file, 'r') as file:
        for line in file.readlines():
            line = line.split()
            if line[0] not in registers:
                registers[line[0]] = 0
            if line[4] not in registers:
                registers[line[4]] = 0
            statements.append(line)
    return statements, registers


def advent8_1(statements, registers):
    for s in statements:
        if eval('registers[' + 's[4]' + ']' + s[5] + s[6]):
            if s[1] == 'inc':
                registers[s[0]] += int(s[2])
            else:
                registers[s[0]] -= int(s[2])
    return max(n for n in registers.values())


def advent8_2(statements, registers):
    max_num = 0
    for s in statements:
        if eval('registers[' + 's[4]' + ']' + s[5] + s[6]):
            if s[1] == 'inc':
                registers[s[0]] += int(s[2])
            else:
                registers[s[0]] -= int(s[2])

            if registers[s[0]] > max_num:
                max_num = registers[s[0]]
    return max_num
