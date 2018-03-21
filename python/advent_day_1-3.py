import math
import numpy
from itertools import combinations

# DAY ONE


def advent1(num):
    total = 0
    num = str(num)
    for i in range(len(num)):
        if num[i - 1] == num[i]:
            total += int(num[i])
    return total


def advent1_1(num):
    total = 0
    num = str(num)
    halfway = len(num) // 2
    for i in range(halfway * 2):
        if num[i - halfway] == num[i]:
            total += int(num[i])
    return total

# DAY TWO


def format2(file):
    row = []
    with open(file, 'r') as lst:
        for line in lst.readlines():
            line = line.replace('\t', ' ')
            line = line.replace('\n', '')
            line = line.split()
            column = []
            for i in line:
                column.append(int(i))
            row.append(column)
    return row


def advent2_1(array):
    total = 0
    for row in array:
        total += int(max(row)) - int(min(row))
    return total


def advent2_2(array):
    total = 0
    rownum = 0
    for row in array:
        rownum += 1
        for a in row:
            for b in row:
                if not (a % b) and a != b:
                    total += a / b
    return total

# DAY THREE


def advent3_1(number):
    rownumber = math.floor(math.sqrt(number)) + 1
    if not rownumber % 2:
        rownumber += 1
    rowstart = rownumber ** 2
    distance = (((number - rowstart) - rownumber // 2)
                % (rownumber - 1)) + rownumber // 2
    return distance


def advent3_2(number):
    size = 1
    while True:
        size += 10
        array = numpy.zeros((size, size))
        x = size // 2
        y = x
        array[x][y] = 1
        side = 0
        jump = 1
        count = 0
        while y < size - 1 and y > 1 and x < size - 1 and x > 1:
            if side == 0:
                x += 1
                count += 1
                if jump == count:
                    count = 0
                    side += 1
            elif side == 1:
                y -= 1
                count += 1
                if jump == count:
                    count = 0
                    side += 1
                    jump += 1
            elif side == 2:
                x -= 1
                count += 1
                if jump == count:
                    count = 0
                    side += 1
            elif side == 3:
                y += 1
                count += 1
                if jump == count:
                    count = 0
                    side = 0
                    jump += 1
            current = array[x - 1][y - 1] + array[x + 1][y + 1] \
                + array[x - 1][y + 1] + array[x + 1][y - 1] \
                + array[x - 1][y] + array[x + 1][y] + array[x][y - 1]\
                + array[x][y + 1]
            array[x][y] = current
            if current > number:
                return current
