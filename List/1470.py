def shuffle(nums, n):
    aList = []
    for i in range(0, len(nums) // 2):
        aList.append(nums[i])
        aList.append(nums[i + n])
    
    return aList

print(shuffle([2,5,1,3,4,7], n = 3))

# Time complexity O(n), Extra space complexity O(n)
# -> Reduce the Extra space complexity to O(1)
