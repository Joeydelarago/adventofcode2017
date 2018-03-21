from itertools import combinations


def format_input(file):
    row = []
    with open(file, 'r') as lst:
        for line in lst.readlines():
            line = line.replace('\t', ' ')
            line = line.replace('\n', '')
            line = line.split()
            column = []
            for i in line:
                column.append(i)
            row.append(column)
    return row


def advent4_1(array):
    valids = 0
    for passphrase in array:
        if len(passphrase) == len(set(passphrase)):
            valids += 1
    return valids


def advent4_2(array):
    valids = 0
    for passphrase in array:
        valids += 1
        for a, b in combinations(passphrase, 2):
            if sorted(list(a)) == sorted(list(b)):
                valids -= 1
                break
    return valids


if __name__ == '__main__':
    print(advent4_1(format_input('advent_4.txt', 'r')))
    print(advent4_2(format_input('advent_4.txt', 'r')))
