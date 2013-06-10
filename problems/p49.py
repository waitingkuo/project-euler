import math
import algos
import itertools

def get_permutations(number):

    permutations = itertools.permutations(','.join(str(number)).split(','))
    permutations = [int(''.join(x)) for x in permutations] 
    permutations = [x for x in permutations if x > 1000]

    return permutations

def solve():

    primes = algos.get_primes(10000)
    primes_set = set(primes)

    for i in range(1000, 10000):
        permutations = get_permutations(i)
        p = []
        for j in permutations:
            if j in primes_set: 
                primes_set.remove(j)
                p.append(j)

        p = list(set(p))
        if len(p) >= 3: 
            for i in range(len(p)):
                for j in range(i+1, len(p)):
                    for k in range(j+1, len(p)):
                        if p[j] - p[i] == p[k] - p[j]:
                            print p[i], p[j], p[k] 

    return 


if __name__ == '__main__':

    solve()
