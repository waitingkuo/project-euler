import math

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def solve(n):

    m = len(coins)
    ans = [[0 for j in range(n+1)] for i in range(m)]

    ans[0] = [1] * (n+1)

    for i in range(1, m):
        for j in range(n+1):
            ans[i][j] = 0
            for count in range((j / coins[i])+1):
                ans[i][j] += ans[i-1][j - count * coins[i]]

    #print ans

    return ans[m-1][n]


if __name__ == '__main__':

    print solve(200)
