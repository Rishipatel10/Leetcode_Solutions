class Solution:
    def reverseWords(self, s: str) -> str:
        str1 = s.split()
        str1.reverse()
        return " ".join(str1)