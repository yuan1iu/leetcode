# 724. Find Pivot Index
def pivotIndex(nums) -> int:
    all = sum(nums)
    left = 0
    for i in range(len(nums)):
        if all - nums[i] - left == left:
            return i
        left += nums[i]
    return -1