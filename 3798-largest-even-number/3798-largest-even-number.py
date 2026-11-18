class Solution:
    def largestEven(self, s: str) -> str:
        str1 = ""
        ans = ""
        for i in range(len(s)):
            str1 += s[i]
            if int(str1) % 2 == 0:
                ans = str1
        return ans