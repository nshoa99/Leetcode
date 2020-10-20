'''
Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''
# import collections
# def moveZeros(nums):
#     cnt = collections.Counter(nums)
#     for i in range(cnt[0]):
#         i, j = 0, 1
#         while i < j and j < len(nums):
#             if nums[i] == 0:
#                 nums[i], nums[j] = nums[j], nums[i]
#             i +=1
#             j +=1
#     return nums
                

def moveZeros(nums):
    i, j = 0, 0 
    while j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
        if nums[i] != 0:
            i +=1
        j +=1
    return nums

# Time complexity O(n), Space complexity O(1)


print(moveZeros([0,1,0,3,12]))




