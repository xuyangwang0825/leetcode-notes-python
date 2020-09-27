
def findRepeatNumber(nums):
    i = 0
    while i < len(nums):
        if nums[i] == i:
            i += 1
            continue
        if nums[nums[i]] == nums[i]: return nums[i]
        nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1

nums = [2, 3, 1, 1, 2, 5, 3]
print(findRepeatNumber(nums))