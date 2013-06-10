import math
from collections import Counter


def solve(layers):

    n = len(layers)
    total = {i: Counter() for i in range(len(layers))}

    total[0][0] = layers[0][0]
    for i in range(n-1):
        for j in range(i+1):
            total[i+1][j] = max(total[i+1][j], total[i][j] + layers[i+1][j])
            total[i+1][j+1] = total[i][j] + layers[i+1][j+1]

    return total[n-1].most_common(1)[0][1]


def parse(filename):
    f = open(filename)
    layers = []
    for line in f:
        layers.append([int(i) for i in line.split(' ')])

    return layers

if __name__ == '__main__':

    layers = parse('p18_input.txt')
    print solve(layers)
