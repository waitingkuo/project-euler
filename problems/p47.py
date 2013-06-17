import math
import algos
import collections

LIMIT = 1000000
primes = algos.get_primes(LIMIT)
#distinct_factors = {i: len(set(algos.factorize(i))) for i in range(2, LIMIT)}

#distinct_factors = {i: len(set(algos.factorize(i))) for i in range(2, LIMIT)}

distinct_factors = {}
for prime in primes:
    for j in range(prime, LIMIT, prime):
        distinct_factors[j] = distinct_factors.get(j, 0) + 1

def solve(n):

    cont = 0
    for i in range(2, LIMIT):
        if distinct_factors[i] == n:
            cont += 1 
            if cont == n:
                return i-n+1
        else:
            cont = 0


    raise Exception('should increase LIMIT')


if __name__ == '__main__':

    print solve(2)
    print solve(3)
    print solve(4)
