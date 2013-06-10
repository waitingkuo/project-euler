import math
import string
import algos


def solve(names):

    letter_scores = dict(zip(string.ascii_uppercase, range(1, 27)))

    ans = 0
    for i, name in enumerate(names, 1):
        score = 0
        for j in name:
            score += letter_scores[j]
        score *= i

        ans += score

    return ans

def parse(filename):

    with open(filename) as f:
        names = f.readline().replace('"', '').split(',')

    return names

if __name__ == '__main__':

    names = parse('p22_input.txt')
    names.sort()

    print solve(names)
