class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        str1 = ""
        n = 0
        m = 0
        while n < len(word1) or m < len(word2):
            if n < len(word1):
                str1 += word1[n]
                n += 1
            if m < len(word2):
                str1 += word2[m]
                m += 1
        return str1