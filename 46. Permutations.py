# 46. Permutations
"""
def permute(self, nums):
    all_res = []
    choice = nums[:]
    def backtrack(idx, res, choice):
        if len(choice) == 0: # no choice left
            all_res.append(res)
        for c in choice:
            
            backtrack(idx + 1, res, choice)
"""


def permute(nums):
    ans = []
    helper(nums, [], ans)
    return ans


def helper(nums, temp, ans):
    if len(nums) == 0:
        ans.append(temp)
        return

    for i in range(len(nums)):
        helper(nums[:i]+nums[i+1:], temp+[nums[i]], ans)


permute([1, 2, 3])
