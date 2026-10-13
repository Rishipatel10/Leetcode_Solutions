class Solution:
    def clearDigits(self, s: str) -> str:
        str1 = []
        demo = "1234567890"
        for i in range(len(s)):
            if s[i] in demo:
                str1.pop()
                continue
            str1.append(s[i])
        ans = ""
        for i in range(len(str1)):
            ans += str1[i]
        return ans