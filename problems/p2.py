def solve(n):

    fib = [1, 2]
    ans = 3
    while True:
        next = fib[-2] + fib[-1]
        if next > n: break
        fib.append(next)

    ans = sum(x for x in fib if x % 2 == 0)

    return ans 

if __name__ == '__main__':

    print solve(4000000) 
