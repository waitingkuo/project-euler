import math


def solve(matrix, cons):

    # matrix: m*n
    ans = 0
    m = len(matrix)
    n = len(matrix)

    def _test_right(i, j):
        result = 1
        for k in range(cons):
            result *= matrix[i][j+k]
        return result
    def _test_down(i, j):
        result = 1
        for k in range(cons):
            result *= matrix[i+k][j]
        return result
    def _test_diag(i, j):
        result = 1
        for k in range(cons):
            result *= matrix[i+k][j+k]
        return result
    def _test_anti_diag(i, j):
        result = 1
        for k in range(cons):
            result *= matrix[i-k][j+k]
        return result
            
    for i in range(m):
        for j in range(n):
            if i + cons - 1 < m:
                ans = max(ans, _test_down(i, j))
            if j + cons - 1 < n:
                ans = max(ans, _test_right(i, j))
            if i + cons - 1 < m and j + cons -1 < n:
                ans = max(ans, _test_diag(i, j))     
            if i - cons + 1 >= 0 and j + cons - 1 < n: 
                ans = max(ans, _test_anti_diag(i, j))         

    return ans


if __name__ == '__main__':

    f = open('p11_input.txt') 
    matrix = []
    for line in f:
        matrix.append([int(e) for e in line.split(' ')])

    print solve(matrix, 4)
