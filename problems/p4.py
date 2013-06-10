import math

def is_palindrome(x):
    x = str(x)
    for i in range(len(x)/2):
        if x[i] != x[len(x)-1-i]: return False
    return True
        

def solve():


    palindromes = []
    for i in range(100, 1000):
        for j in range(100, 1000):
            if is_palindrome(i*j): palindromes.append(i*j)

    return sorted(palindromes)[-1]
            



if __name__ == '__main__':

    print solve()
