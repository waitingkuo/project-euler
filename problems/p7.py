import math
from algos import get_primes


def solve(n):

    primes = get_primes(20 * n)

    return primes[n-1]


if __name__ == '__main__':

    print solve(10001)
