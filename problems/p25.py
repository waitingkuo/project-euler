import math


def solve(m):

    f = {}    
    f[1] = 1
    f[2] = 1
    n = 3
    while True:

        f[n] = f[n-1] + f[n-2]
        if len(str(f[n])) >= m: return n

        n += 1



if __name__ == '__main__':

    print solve(3)
    print solve(1000)
