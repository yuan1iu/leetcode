# 75. Sort Colors
class Solution:
    def sortColors(self, nums: List[int]) -> None:  # version 1 brute force
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0 = count_1 = count_2 = 0
        for idx, num in enumerate(nums):
            if num == 0:
                count_0 += 1
            elif num == 1:
                count_1 += 1
            else:
                count_2 += 1
        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_0+count_1):
            nums[i] = 1
        for i in range(count_0+count_1, count_0+count_1+count_2):
            nums[i] = 2
