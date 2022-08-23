# 70. Climbing Stairs
class Solution:
    cache = {0: 1}

    def climbStairs(self, n):
        if n in self.cache: return self.cache[n]
        if n < 0:
            return 0
        elif n == 0:
            return 1
        self.cache[n-1] = self.climbStairs(n-1)
        self.cache[n-2] = self.climbStairs(n-2)

        self.cache[n] = self.cache[n-1]+ self.cache[n-2]
        
        return self.cache[n]