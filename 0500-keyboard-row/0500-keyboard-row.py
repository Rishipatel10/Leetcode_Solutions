class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        s1 = "qwertyuiop"
        s2 = "asdfghjkl"
        s3 = "zxcvbnm"
        ans = []
        for i in range(len(words)):
            c1 = 0
            c2 = 0
            c3 = 0
            word = words[i].lower()
            for ch in word:
                if ch in s1:
                    c1 += 1
                if ch in s2:
                    c2 += 1
                if ch in s3:
                    c3 += 1
            if c1 == len(words[i]) or c2 == len(words[i]) or c3 == len(words[i]):
                ans.append(words[i])
        return ans