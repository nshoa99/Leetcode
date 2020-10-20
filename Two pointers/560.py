'''
Subarray Sum Equals K 
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7]
'''
# if all the elements in the nums are positive

def subarraySun(nums, k):
    cnt = 0
    i, j = 0, 0 
    aSum = 0 
    while i < len(nums):
        if aSum + nums[i] > k:
            aSum -= nums[j]
            j +=1
        elif aSum + nums[i] < k:
            aSum += nums[i]
            i +=1
        else:
            cnt +=1
            aSum += nums[i]
            i +=1
    return cnt
