import math

def sum_of_squares(n):

    return sum(i**2 for i in range(1, n+1))

def square_of_sums(n):

    return sum(i for i in range(1, n+1)) ** 2

def solve(n):
    
    return square_of_sums(n) - sum_of_squares(n)


if __name__ == '__main__':

    print solve(10)
    print solve(100)
