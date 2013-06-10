import math

chains = {}

def compute_chain(n):

    count = 1
    while n != 1:

        if n % 2 == 0: 
            n /= 2
        else:
            n = 3*n+1
        count += 1

    return count 

def solve(n):

    ans = 0
    max_chain = 0

    for i in range(1, n):
        chain = compute_chain(i)
        if chain > max_chain:
            ans = i 
            max_chain = chain
            print ans, max_chain

    return ans


if __name__ == '__main__':

    print solve(1000000)
