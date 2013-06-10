import math


def solve(n):

    res = 1
    for i in range(1, n+1):
        res *= i

    ans = sum(int(i) for i in list(str(res)))

    return ans


if __name__ == '__main__':

    print solve(100)
