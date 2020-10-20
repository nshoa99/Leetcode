'''
Next Greater Element II 

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

''' 


def nextGreaterElemets(nums):
    result = [-1] * len(nums)
    stack = []
    for _ in range(2):
        i = len(nums) - 1
        while i >= 0:
            if len(stack) == 0:
                stack.append(i)
                i -= 1
            elif nums[i] < nums[stack[-1]]:
                result[i] = nums[stack[-1]]
                stack.append(i)
                i -= 1
            else:
                stack.pop()
    return result

print(nextGreaterElemets([1,2,1]))


# Time complexity O(n), Extra space complexity O(1)
