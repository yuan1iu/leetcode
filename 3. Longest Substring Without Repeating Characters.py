# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        list = []
        for i in range(len(s)):
            if s[i] in list:
                index = list.index(s[i])
                longest = max(len(list), longest)
                list = list[index+1:]
            list.append(s[i])
        return max(len(list), longest)

    def BruteForce(self, s: str) -> int:
        maxLength = 0
        unique = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] not in unique:
                    unique.add(s[j])
                else:
                    maxLength = max(maxLength, len(unique))
                    unique.clear()
                    break
        return max(maxLength, len(unique))

    def sliding_window(self, s: str) -> int:
        chars = [0] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)

            right += 1
        return res

    def optimized_sliding_window(self, s: str) -> int:
        map = {}
        max_length = 0
        left = 0
        for idx, ss in enumerate(s):
            if ss in map:  # char already exists
                left = map[ss] + 1 if map[ss] + 1 > left else left
            map[ss] = idx
            max_length = max(max_length, idx - left + 1)
        return max_length
