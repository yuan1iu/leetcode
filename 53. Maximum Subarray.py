# 53. Maximum Subarray

import math
from typing import List


class MaxSubArray:
    def BruteForce(self, nums: List[int]) -> int:
        max_subarray = -math.inf
        for i in range(len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray += nums[j]
                max_subarray = max(max_subarray, current_subarray)
        return max_subarray

    def KadanesAlgorithm(self, nums: List[int]) -> int:
        maxArr = cur = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i] + cur, nums[i])
            maxArr = max(cur, maxArr)
        return maxArr
