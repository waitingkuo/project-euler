import math

def to_bin(n):

    return int(bin(n)[2:])

def is_palindromes(n):
    
    n = str(n)
    for i in range(len(n)/2):
        if n[i] != n[len(n)-1-i]: return False

    return True

def solve(n):

    ans = 0
    for i in range(1, n):
        if is_palindromes(i) and is_palindromes(to_bin(i)):
            ans += i

    return ans


if __name__ == '__main__':

    print solve(1000000)
