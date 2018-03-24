import re

def format_input(file):
    output = ''
    with open(file, 'r') as file:
        for line in file.readlines():
            output += line
        output = re.sub(r'!.', '', output)
    return output

def advent9_1(data):
    data = re.sub(r'<.*?>', '', data)  # Removing the garbage
    depth = 0
    score = 0
    for i in data:
        if i == '{':
            depth += 1
        if i == '}':
            score += depth
            depth -= 1
    return score


def advent9_2(data):
    start_len = len(data)
    data = re.sub('(?<=\<)(.*?)(?=\>)', '', data)
    return start_len - len(data)
