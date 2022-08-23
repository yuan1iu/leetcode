# 22. Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int):
        
        def dfs(open, close, ans):
            if close == n:
                res.append(ans)
                return
            if open < n:
                dfs(open+1, close, ans+'(')
            if open > close:
                dfs(open, close+1, ans+ ')')
        
        res = []
        dfs(0,0,'')
        return res