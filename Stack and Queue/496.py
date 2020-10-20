'''
Next Greater Element I
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''


def nextGreaterElement(nums1, nums2):
    finals = [-1] * len(nums1)                              # Space O(n)
    mapping = {nums1[i]: i for i in range(len(nums1))}      # Space O(n)
    stack = []                                              # Space O(n)
    i = 0
    while i < len(nums2):                                   # Time complexity O(n)
        if len(stack) == 0 or nums2[i] < stack[-1]:
            stack.append(nums2[i])
            i += 1
        else:
            if stack[-1] in mapping:
                finals[mapping[stack[-1]]] = nums2[i]
            stack.pop()

    return finals

# Time complexity O(n) , Extra space complexity O(n)


print(nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))