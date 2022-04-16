# 58. Length of Last Word
from collections import Counter
import math
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

    def lengthOfLastWord2(self, s: str) -> int:
        end = len(s) - 1
        while s[end] == " ":
            end -= 1
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        return end - start

    def lengthOfLastWord3(self, s: str) -> int:
        p, length = len(s), 0

        while p > 0:
            p -= 1
            if s[p] != ' ':
                length += 1
            elif length > 0:
                return length
        return length
