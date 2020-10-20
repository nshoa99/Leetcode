''' Intersection of Two Array
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

def intersection(nums1, nums2):
    i, j = 0, 0 
    nums1, nums2 = sorted(nums1), sorted(nums2)
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i +=1
        elif nums1[i] > nums2[j]:
            j +=1
        else:
            result.append(nums2[j])
            i +=1
            j +=1
    return result
    
print(intersection( nums1 = [1,2,2,1], nums2 = [2,2]))



