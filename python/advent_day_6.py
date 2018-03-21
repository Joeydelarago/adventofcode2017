from numpy import argmax


def format_input(file):
    with open(file, 'r') as file:
        output = file.readline().split()
        output = list(map(int, output))
    return output


def find_largest(lst):
    """ retrun the index of the largest number in a list, if there are two
        return the first.
    """
    biggest = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[biggest]:
            biggest = i
    return biggest


def advent6_1(lst):
    seenlst = []
    cycles = 0
    while True:
        cycles += 1
        largest = find_largest(lst)
        blocks = lst[largest]
        lst[largest] = 0

        index = largest + 1
        for i in range(blocks):
            index += 1
            lst[index % len(lst) - 1] += 1

        if lst in seenlst:
            break
        else:
            seenlst += [lst.copy()]

    return cycles


def advent6_2(lst):
    seenlst = []
    cycles = 0
    while True:
        cycles += 1
        largest = find_largest(lst)
        blocks = lst[largest]
        lst[largest] = 0

        index = largest + 1
        for i in range(blocks):
            index += 1
            lst[index % len(lst) - 1] += 1

        if lst in seenlst:
            print('cycles since last seen', cycles)
            cycles = -1
            seenlst = [[lst]]
        else:
            seenlst += [lst.copy()]

    return cycles


print(advent6_2(format_input('advent_6.txt')))
