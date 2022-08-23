# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        i, j = 0, 0
        res, curSum = float('Inf'), 0
        while j < len(nums):
            curSum += nums[j]
            if curSum >= target:
                while curSum >= target:
                    res = min(j - i + 1, res)
                    curSum -= nums[i]
                    i += 1
            j += 1

        return res if res != float('Inf') else 0


class Solution2:

    def minSubArrayLen(self, target, nums):
        result = len(nums) + 1
        for idx, n in enumerate(nums[1:], 1):
            nums[idx] = nums[idx - 1] + n
        left = 0
        for right, n in enumerate(nums):
            if n >= target:
                left = self.find_left(left, right, nums, target, n)
                result = min(result, right - left + 1)
        return result if result <= len(nums) else 0

    def find_left(self, left, right, nums, target, n):
        while left < right:
            mid = (left + right) // 2
            if n - nums[mid] >= target:
                left = mid + 1
            else:
                right = mid
        return left
