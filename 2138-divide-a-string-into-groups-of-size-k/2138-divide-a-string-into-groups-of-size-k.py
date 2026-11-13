class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        ans = []
        idx = 0
        for i in range(0,len(s),k):
            c = 0
            str1 = ""
            while c != k:
                if idx < len(s):
                    str1 += s[idx]
                    idx += 1
                else:
                    str1 += fill
                c += 1
            ans.append(str1)
        return ans