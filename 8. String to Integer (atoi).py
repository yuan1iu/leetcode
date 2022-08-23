# 8. String to Integer (atoi)
def myAtoi(s: str) -> int:
    i = 0
    sign = 1
    res = 0
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if not s: return 0
    while i < len(s) and s[i] == ' ':
        i += 1
    if i < len(s): 
        if s[i] == '-' or s[i] == '+':
            if s[i] == '-':
                sign = -1 
            i += 1
    if i < len(s) and not s[i].isdigit(): return 0
    while i < len(s) and s[i].isdigit():
        cur = int(s[i])
        if res*10 > INT_MAX or res == INT_MAX//10 and cur > 7:
            return INT_MAX if sign == 1 else INT_MIN
        res = res*10 + cur
        i += 1
    return res*sign