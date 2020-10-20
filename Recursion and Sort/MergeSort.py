nums = [20, 10, 16, 6, -89, 9, -1, 5, 100]
def devide(i, j, nums):
    middle = (i + j) // 2 # i + (j - i) // 2
    # TH cơ bản
    if i == j:
        return [nums[i]]

    nums1 = devide(i, middle, nums)
    nums2 = devide(middle + 1, j, nums)

    return merge(nums1, nums2)

def merge(nums1, nums2):
    i, j = 0, 0 
    new_nums = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            new_nums.append(nums1[i])
            i +=1
        else:
            new_nums.append(nums2[j])
            j +=1
    if i < len(nums1):
        new_nums += nums1[i:]
    if j < len(nums2):
        new_nums += nums2[j:]

    return new_nums


print(devide(0, len(nums) - 1, nums))

# Time complexity O(Nlog(N))