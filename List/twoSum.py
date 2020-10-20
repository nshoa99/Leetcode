def twoSum(nums, target):
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         if nums[i] + nums[j] == target:
    #             return (i,j)
    # return -1
    #O(N^2)

    aDict = dict()                      # O(N)
    for i in range(len(nums)):          # O(N)
        if nums[i] in aDict:            # O(1)
            return (aDict[nums[i]], i )
        else:
            aDict[target - nums[i]] = i
            print(aDict)
    return -1
    # O(N)

print(twoSum([2,7,11,22], 9))
