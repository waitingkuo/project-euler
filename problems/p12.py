import math
import algos


def solve(n):

    limit = 10000000

    primes = algos.get_primes(limit)

    i = 1
    s = 0
    while True:
        s += i
        if s > limit: assert 'increase limit'
        divisors = algos.number_of_divisors(s, primes)
        print s, divisors
        if divisors >= n:
            return s
        i += 1


if __name__ == '__main__':

    print solve(500)
