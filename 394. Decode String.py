# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)

            elif ch == ']':
                substr = ''
                while stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                time = ''
                while stack and stack[-1].isdigit():
                    time = stack.pop() + time
                res = int(time)*substr
                stack.append(res)

        return ''.join(stack)
