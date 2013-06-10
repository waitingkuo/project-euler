import math


def solve(n):

    mid = int(math.sqrt(n))

    factors = [1]
    for i in range(2, mid+1):
        if n == 1: break

        while n % i == 0:
            factors.append(i)
            n /= i

    factors.append(n)

    return sorted(factors)[-1]

if __name__ == '__main__':

    print solve(600851475143)
