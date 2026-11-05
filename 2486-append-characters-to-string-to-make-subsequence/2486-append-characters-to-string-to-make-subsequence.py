class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        c = 0
        for i in range(len(s)):
            if c < len(t) and s[i] == t[c]:
                c += 1

        return len(t) - c