# 50. Pow(x, n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        def pow(n):
            if x == 0: return 0
            if n == 0: return 1
            if n == 1: return x
            half = pow(n//2)
            if n % 2 == 0:
                return half * half
            return half * half * x
        
        return pow(n)

s = Solution()
s.myPow(2,5)