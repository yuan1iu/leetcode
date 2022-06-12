# 494. Target Sum
class Solution:
    def __init__(self) -> None:
        self.dp = {}
    def findTargetSumWays_brute(self, nums, target: int) -> int:
        def dfs(i, val):
            if i == len(nums):
                return 1 if val == target else 0
            return dfs(i+1, val+nums[i]) + dfs(i+1, val-nums[i])                
        return dfs(0, 0)

    def findTargetSumWays_caching(self, nums, target: int) -> int:
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in self.dp:
                return self.dp[(i,total)]
            self.dp[(i,total)] = dfs(i+1,total+nums[i])+dfs(i+1,total-nums[i])
            return self.dp[(i,total)]   
        return dfs(0,0)

    def findTargetSumWays_dp(self, nums, target: int) -> int:
        total = sum(nums)
        dp = [[0] * (2*total+1) for _ in range(len(nums))]
        dp[0][total + nums[0]] = 1
        dp[0][total - nums[0]] += 1
        for i in range(1, len(nums)):
            for j in range(len(dp[0])):
                if dp[i-1][j] > 0:
                    dp[i][j+nums[i]] += dp[i-1][j]
                    dp[i][j-nums[i]] += dp[i-1][j]

    def findTargetSumWays_dp2(self, nums, target: int) -> int:

        total = sum(nums)
        if total < abs(target): return 0
        dp = [0] * (2*total+1)
        dp[total + nums[0]] = 1
        dp[total - nums[0]] += 1
        for i in range(1,len(nums)):
            new = [0] * (2*total+1)
            for j in range(len(dp)):
                if dp[j] > 0:
                    new[j+nums[i]] += dp[j]
                    new[j-nums[i]] += dp[j]
            dp = new
            
        return dp[target+total]