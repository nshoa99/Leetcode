'''
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''

# def matrixReshape(nums, r, c):
#     if len(nums) * len(nums[0]) != r * c:
#         return nums

#     A = []
#     for i in range(0, len(nums)):
#         for j in range(0, len(nums[0])):
#             A.append(nums[i][j])
    
#     Z = [
#         [0 for _ in range(c)] for _ in range(r)
#     ]
    
#     k = 0
#     for i in range(0, r):
#         for j in range(0, c):
#             Z[i][j] = A[k]
#             k += 1
    
#     return Z


def matrixReshape(nums, r, c):
    r_nums = len(nums)
    c_nums = len(nums[0])

    if r_nums * c_nums != r * c:
        return nums
    else:
        result = [
            [0 for _ in range(c)] for _ in range(r)
        ]
        count = 0
        for i in range(0, c_nums):
            for j in range(0, r_nums):
                x = count // c
                y = count % c
                result[x][y] = nums[i][j]
                count += 1
        return result




print(matrixReshape([[1,2],[3,4]], 1, 4))