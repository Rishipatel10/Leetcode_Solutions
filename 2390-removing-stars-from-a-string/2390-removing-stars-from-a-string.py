class Solution:
    def removeStars(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if s[i] == '*':
                ans.pop()
                continue
            ans.append(s[i])
        return "".join(ans)