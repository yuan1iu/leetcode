# 14. Longest Common Prefix

def longestCommonPrefix(strs) -> str:
    if len(strs) == 0: return ""
    prefix = strs[0]
    for str in strs:
        while not str.startswith(prefix):
            prefix = prefix[:len(prefix)-1]
        if prefix == "": return ""
    return prefix