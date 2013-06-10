import math

words = {
    1: len('one'),
    2: len('two'),
    3: len('three'),
    4: len('four'),
    5: len('five'),
    6: len('six'),
    7: len('seven'),
    8: len('eight'),
    9: len('night'),
    10: len('ten'),
    11: len('eleven'),
    12: len('twelve'),
    13: len('thirteen'),
    14: len('fourteen'),
    15: len('fifteen'),
    16: len('sixteen'),
    17: len('seventeen'),
    18: len('eighteen'),
    19: len('nighteen'),
    20: len('twenty'),
    30: len('thirty'),
    40: len('fourty'),
    50: len('fifty'),
    60: len('sixty'),
    70: len('seventy'),
    80: len('eighty'),
    90: len('nighty'),
    100: len('hundred'),
    1000: len('thousand'),
}


def compute(n):
    
    if n == 1000: return words[1] + words[1000]

def solve(i):

    ans = 0
    for i in range(1, n+1):
        count = compute(i)
        

    return ans


if __name__ == '__main__':

    print solve(1000)
