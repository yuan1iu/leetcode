# License Key Formatting
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        counter = 0
        ans = ''
        for i in range(len(s)-1, -1, -1):
            if s[i] != '-':
                # determine if we need to add '-' first then add it before char
                # it will prevent the situation like -XXXX-XXXX
                if counter > 0 and (counter)%k == 0: 
                    ans += '-'
                ans += s[i].upper()                    
                counter += 1
        return ans[::-1]