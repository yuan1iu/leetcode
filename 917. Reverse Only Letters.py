class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack = [c for c in s if c.isalpha()]
        res = ""
        for c in s:
            if c.isalpha():
                res += stack.pop()
            else:
                res += c
        return res
