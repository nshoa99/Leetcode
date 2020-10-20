def threeSum(nums):
    nums.sort()
    aSet = set()
    for k in range(len(nums) - 2):
        exp = 0 - nums[k]
        i = k + 1
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] > exp:
                j -= 1
            elif nums[i] + nums[j] < exp:
                i += 1
            else:
                aSet.add((nums[k], nums[i], nums[j]))
                i += 1
                j -= 1
        
    return aSet


print(threeSum(nums = [-1,0,1,2,-1,-4]))

