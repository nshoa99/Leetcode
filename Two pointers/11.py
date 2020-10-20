'''
Container with most water
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

2 <= height.length <= 3 * 104
0 <= height[i] <= 3 * 104 
'''


# def maxArea(height):
#     max_area = 0 
#     for i in range(0, len(height)):
#         for j in range(i, len(height)):
#             S = min(height[i], height[j]) * (j - i)
#             max_area = max(max_area, S)

#     return max_area

# Time complexity O(n), Extra space complexity O(1)
# Time limit exeeded -> Reduce time complexity 


def maxArea(height):
    n = len(height)
    i, j = 0, n - 1
    max_area = 0
    while i < j:
        S = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, S)
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
    return max_area

# Time complexity O(n), Extra Space complexity O(1)



print(maxArea([3,9,3,4,7,5,12,1,6]))

