class Solution:
    def countAsterisks(self, s: str) -> int:
        c = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == '|':
                c += 1
            elif s[i] == '*' and c % 2 == 0:
                ans += 1
        return ans
    