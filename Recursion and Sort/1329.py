import collections
def diagonalSort(mat):
    row = len(mat)
    col = len(mat[0])
    aDict = collections.defaultdict(list)
    for i in range(row):
        for j in range(col):
            aDict[j - i].append(mat[i][j])
    
    for item in aDict:
        aDict[item].sort(reverse = True)
    
    for i in range(row):
        for j in range(col):
            mat[i][j] = aDict[j - i][-1]
            aDict[j - i].pop()
    return mat

print(diagonalSort([[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]))

# Các phần tử trên cùng 1 đường chéo có cùng giá trị Diff = (j - i) với i là số hàng, j là số cột
# =>1. Tạo 1 dict với key là Diff, giá trị là 1 mảng chứa các giá trị trên đường chéo đó
#   2. Lặp qua các phần tử đã lưu và sắp xếp
#   3. Gán lại vào mảng ban đầu