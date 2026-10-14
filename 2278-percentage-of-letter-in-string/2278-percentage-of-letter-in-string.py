class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        total = len(s)
        n = 0
        for i in range(len(s)):
            if s[i] == letter:
                n += 1
        ans = (n / total) * 100

        return int(ans)