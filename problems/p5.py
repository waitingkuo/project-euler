import math

def gcd(a, b):
    if a % b == 0: return b
    return gcd(b, a%b)
def lcm(a, b):
    return a*b/gcd(a,b)        


def solve(n):

    ans = 1

    for i in range(1, 21):
        ans = lcm(ans, i)

    return ans


if __name__ == '__main__':

    print solve(20)
