import math


def solve(numbers):
    

    s = sum(int(n) for n in numbers)

    return str(s)[:10]


if __name__ == '__main__':

    f = open('p13_input.txt')
    numbers = []
    for line in f:
        numbers.append(line.strip()) 
    
    print solve(numbers)
