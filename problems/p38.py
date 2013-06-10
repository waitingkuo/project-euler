import math

def compute(number, n):

    numbers = [number * i for i in range(1, n+1)]
    ans = ''
    for num in numbers: ans += str(num)

    return int(ans)

def check_pandigital(n):

    digits = set()
    for i in str(n):
        if i!='0':
            digits.add(i)


    if len(digits) == 9: return True
    else: return False
        

def solve():

    numbers = []
    for i in range(1, 10000):
        for j in range(2, 10):
            n = compute(i, j)
            if n < 100000000: continue
            if n > 1000000000: break
            if check_pandigital(n): 
                numbers.append(n)
                print i, j, n

    return max(numbers)


if __name__ == '__main__':

    print solve()
