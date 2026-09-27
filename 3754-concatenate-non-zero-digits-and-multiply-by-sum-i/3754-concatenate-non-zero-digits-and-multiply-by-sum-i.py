class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        s = str(n)
        ans = 0
        str1 = ""
        for i in range(len(s)):
            if s[i] != '0':
                ans += int(s[i])
                str1 += s[i]
        return int(str1) * ans