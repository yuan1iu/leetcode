def longestPalindrome(s):
    front = []
    back = []
    for i in range(len(s)):
        for j in range(i, len(s)):
            front.append(s[i:j+1])
            back.append(s[:-i])


longestPalindrome("abc")
ss = "abc"
print(ss[-2:0])
