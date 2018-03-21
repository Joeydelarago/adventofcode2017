def format_input(file):
    outlst = []
    with open(file, 'r') as lst:
        for line in lst.readlines():
            outlst.append(int(line.strip()))
    return outlst


def advent5_1(lst):
    pointer = 0
    jumpcount = 0
    while True:
        lst[pointer] += 1
        pointer += lst[pointer] - 1
        jumpcount += 1
        if pointer < 0 or pointer > len(lst) - 1:
            return jumpcount


def advent5_2(lst):
    pointer = 0
    jumpcount = 0
    offset = lst[0]
    while True:
        offset = lst[pointer]

        if offset > 2:
            lst[pointer] -= 1
        else:
            lst[pointer] += 1

        pointer += offset
        jumpcount += 1

        if pointer < 0 or pointer > len(lst) - 1:
            return jumpcount


if __name__ == '__main__':
    print(advent5_1(format_input('advent_5.txt')))
    print(advent5_2(format_input('advent_5.txt')))
