import math
import algos


def solve(n, m):

    primes = algos.get_primes(m)

    proper_divisors_sum = {}
    for i in range(2, m):
        proper_divisors_sum[i] = algos.divisors_sum(i, primes=primes) - i
        
        
    amicable_numbers = []
    for i in range(2, n):
        proper = proper_divisors_sum[i]
        if proper != 1 and proper != i:
            proper_proper = proper_divisors_sum[proper]
            if proper_proper == i:
                print i, proper, proper_proper
                amicable_numbers.append(i)

    return sum(amicable_numbers)


if __name__ == '__main__':

    #print solve(100)
    print solve(10000, 25321)
