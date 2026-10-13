class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = text.split()
        ans = 0
        for i in s:
            c = 0
            for j in range(len(brokenLetters)):
                if brokenLetters[j] in i:
                    c += 1
                    break
            if c == 0:
                ans += 1
        return ans