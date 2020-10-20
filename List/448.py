'''
448. Find All Numbers Disappeared in an Array
Easy

3292

261

Add to List

Share
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''


import collections

# def findDisappearedNumbers(nums):
#     counter = collections.Counter(nums)
#     finals = []
#     for i in range(1,  len(nums) + 1):
#         if counter[i] == 0:
#             finals.append(i)
#     return finals

#Time complexity O(N), space compelixy O(N) of counter


def findDisappearedNumbers(nums):
    finals = []
    for i in range(0, len(nums)):
        if nums[abs(nums[i]) - 1] > 0:
            nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1]
    
    for i in range(0, len(nums)):
        if nums[i] > 0:
            finals.append(i + 1)
    
    return finals

#Time complexity O(N), space complexity O(1) 


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))