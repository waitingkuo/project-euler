import math
from algos import get_primes


def solve(n):


    primes = get_primes(n)
    primes_set = set(primes)
    size = len(primes_set)

    print size

    ans = 41
    max_length = 5

    for i in range(0, size):
        total = 0
        if i % 1000 == 0:
            print i
        for j in range(i, size):
            total += primes[j]
            if total in primes_set:
                length = j-i+1
                if max_length < length: 
                    max_length = length
                    ans = total

            if total > n: break

    return ans


if __name__ == '__main__':

    print solve(1000000)
