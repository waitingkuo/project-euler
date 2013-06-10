import math
from algos import get_primes


def solve(n):

    primes = get_primes(n)

    return sum(primes)


if __name__ == '__main__':

    print solve(2000000)
