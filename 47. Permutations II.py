class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(path, choice):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            used = set()
            for i in range(len(choice)):
                if choice[i] in used:
                    continue
                used.add(choice[i])
                permute(path+[choice[i]], choice[:i]+choice[i+1:])
        res = []
        permute([], nums)
        return res
