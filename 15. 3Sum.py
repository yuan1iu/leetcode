# 15. 3Sum
class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    # make sure we don't loop the same l or r
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return res

    def threeSum_not_sorted(self, nums):
        res = set()
        dups = set()
        for i in range(len(nums)):
            if nums[i] in dups:
                continue
            dups.add(nums[i])

            mapping = set()
            for j in range(i+1, len(nums)):
                target = -nums[i] - nums[j]
                if target not in mapping:
                    mapping.add(nums[j])
                else:  # find solution
                    res.add(tuple(sorted((nums[i], nums[j], target))))
        return res
