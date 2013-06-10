import math


def solve(start_year, end_year):

    def get_months(year):
        if year % 400 == 0: return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        elif year % 100 == 0: return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        elif year % 4 == 0: return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
        else: return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  

    days = 0
    for year in range(1900, start_year):
        days += sum(get_months(year)) % 7

    count = 0
    for year in range(start_year, end_year):
        for month in get_months(year):
            if (days + 1) % 7 == 0: count += 1
            days = (days + month) % 7
             

    return count


if __name__ == '__main__':

    print solve(1901, 2001)
