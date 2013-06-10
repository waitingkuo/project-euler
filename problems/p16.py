import math


def solve(n):


    return sum(int(x) for x in ','.join(str(2 ** n)).split(','))


if __name__ == '__main__':

    print solve(1000)
