class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        str1 = ""
        count = 0
        for i in s:
            if i == ' ':
                count+=1
            if count == k:
                break
            else:
                str1+=i
        return str1