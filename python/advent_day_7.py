from numpy import argmax
import re


def format_input(file):
    output = {}
    with open(file, 'r') as file:
        for l in file.readlines():
            l = re.sub('[->(,)]', '', l).split()
            output[l[0]] = Node(l[0], int(l[1]), l[2:])
    return output


def make_tree(data):
    for node in data.values():
        children = []
        for child in node.children:
            data[child].parent = node
            children.append(data[child])
        node.children = children
    return data


class Node:
    def __init__(self, name, weight, children):
        self.name = name
        self.weight = weight
        self.children = children
        self.parent = None

    def __str__(self):
        return self.name + ' ' + str(self.children)


def advent7_1(data):
    children = []
    for node in data.values():
        for child in node.children:
            children.append(child)

    for node in data.values():
        found = False
        for c in children:
            if c == node.name:
                found = c
        if not found:
            return node


def advent7_2(data):
    make_tree(data)
    odd_node = find_odd_weight(data['ahnofa'])
    siblings = odd_node.parent.children
    if siblings[0] != odd_node:
        dif = check_weight(siblings[0]) - check_weight(odd_node)
        return odd_node.weight + dif


def find_odd_weight(node):
    nodes = len(node.children)
    if nodes == 0:
        return node

    elif nodes == 1:
        return find_odd_weight(node)

    elif nodes == 2:
        w1 = find_odd_weight(node.children[0])
        w2 = find_odd_weight(node.children[1])
        if w1:
            return w1
        return w2

    else:
        w1 = check_weight(node.children[0])
        w2 = check_weight(node.children[1])
        w3 = check_weight(node.children[2])
        if w1 == w2:
            for child in node.children:
                if check_weight(child) != w1:
                    return find_odd_weight(child)
        elif w2 == w3:
            for child in node.children:
                if check_weight(child) != w3:
                    return find_odd_weight(child)
        else:
            return find_odd_weight(node.children[1])

        return node


def check_weight(node):
    weight = node.weight
    for child in node.children:
        weight += check_weight(child)
    return weight
