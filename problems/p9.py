import math


def solve(n):

    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c = n - a - b
            if c <= b: continue
            if (a**2) + (b**2) == (c**2):
                print a, b, c
                return a*b*c



if __name__ == '__main__':

    print solve(1000)
