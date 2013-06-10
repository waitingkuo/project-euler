import math

MOD = 10 ** 10

def self_power(n):
    
    ans = 1
    for i in range(n):
        ans = (ans * n) % MOD
    return ans

def solve(n):

    ans = 0
    for i in range(1, n+1):
        ans += self_power(i)

    ans %= MOD

    return ans


if __name__ == '__main__':

    print solve(1000)
