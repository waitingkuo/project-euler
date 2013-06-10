import math

MOD = 10 ** 9

def squares_sum(n):
    """ Sum of the Squares of the First n Natural Numbers """
    return n * (n+1) * (2*n+1) / 6

def solve(n):

    if n == 1: return 1

    ans = 0

    first = 1
    #last = int(math.sqrt(n))
    last = n
    for i in range(first, last+1):
        #if i % 100000 == 0: print i
        #ans = (ans + (i**2) * (n/i)) % MOD
        print i, i**2, (n/i), (i**2) * (n/i)




if __name__ == '__main__':

    print '===test==='
    print solve(20)
    #print solve(2)
    #print solve(3)
    #print solve(4)
    #print solve(5)
    #print solve(6)
    print
    print '===problem==='
    #print solve(10 ** 15)
    


