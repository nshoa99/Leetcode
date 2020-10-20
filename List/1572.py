def diagonalSum(mat):
    n = len(mat)
    total = 0 
    for i in range(0,n):
        total += mat[i][i] + mat[i][n - 1 - i]
    
    if n % 2 != 0:
        total -= mat[n // 2][n // 2]
    return total

print(diagonalSum([[1,2,3],[4,5,6],[7,8,9]]))

# expected = 25

