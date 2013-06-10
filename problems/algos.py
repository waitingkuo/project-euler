import math
import operator
from collections import Counter

def prod(iterable):
    """ Product of the iterable """
    
    return reduce(operator.mul, iterable, 1)

def primes_sieve(n):

    a = [True] * (n+1)
    a[0] = a[1] = False

    for i, is_prime in enumerate(a):
        if is_prime:
            yield i
            for j in xrange(i*i, n+1, i):
                a[j] = False

def get_primes(n):
    """ Get primes >=1 and <=n """

    return list(primes_sieve(n))
            
def factorize(n, primes=None):

    if primes and primes[-1] < math.sqrt(n): raise Exception('No enough primes')
    if not primes: primes = get_primes(n)
    
    factors = []
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            factors.append(i)
            n /= i

    if n != 1: factors.append(n)

    return factors

def geometric_series_sum(a, r, n):
    """ 
    Sum of the geometris series
    a: init value
    r: ratio
    n: number of series
    """

    if isinstance(a, int) and isinstance(r, int):
        return a * (1 - (r ** n)) / (1 - r)
    else:
        return 1.0 * a * (1 - (r ** n)) / (1 - r)


def number_of_divisors(n, primes=None, factors=None):

    if factors:
        # filter out 1s
        factors = filter(lambda x:x!=1, factors)
        assert prod(factors) == n
    else:
        factors = factorize(n, primes)

    counter = Counter(factors)
    counter.update(counter.keys())
    p = prod(counter.values())

    return p
    
def divisors_sum(n, primes=None, factors=None):
    
    if factors:
        # filter out 1s
        factors = filter(lambda x:x!=1, factors)
        assert prod(factors) == n
    else:
        factors = factorize(n, primes)

    counter = Counter(factors)
    s = prod([geometric_series_sum(1, k, v+1) for k, v in counter.items()])
        
    return s

def C(m, n):

    if m == 0 and n == 0: return 1
    if n == 0 or n == m: return m
    if m < n: raise Exception

    ans = 1

    if n > m - n: n = m - n
    
    for i in range(m, m-n, -1): ans *= i
    for i in range(1, n+1): ans /= i


    return ans
         

if __name__ == '__main__':

    print get_primes(97)      
