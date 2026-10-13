class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ""
        n = 0
        for i in range(0,len(s),2):
            ans += s[i]
            if i < len(s)-1:
                n = ord(s[i]) + int(s[i+1])
                ans += chr(n)
        return ans