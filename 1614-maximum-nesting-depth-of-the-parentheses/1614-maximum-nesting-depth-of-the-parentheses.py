class Solution:
    def maxDepth(self, s: str) -> int:
        c = 0
        maxi = 0
        for i in range(len(s)):
            if s[i] == '(':
                c += 1
            elif s[i] == ')':
                c -= 1
            maxi = max(maxi,c)
        return maxi