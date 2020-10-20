'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''



def productExceptSelf(nums):
    n = len(nums)
    p = 1
    output = []
    for i in range(0, n):
        output.append(p)
        p *= nums[i]
    
    
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] *= p 
        p *= nums[i]
    return output


print(productExceptSelf([1,2,3,4]))


# class Solution:
#     def heightChecker(self, heights: List[int]) -> int:
#         cnt = collections.Counter(heights)
#         i, ans = 1, 0
#         for h in heights:
#             while cnt[i] == 0: 
#                 i += 1         
#             if i != h:         
#                 ans += 1       
#             cnt[i] -= 1        
#         return ans
        