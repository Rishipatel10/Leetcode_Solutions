class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        ans = ""
        mp = {}
        for key, value in knowledge:
            mp[key] = value
        i = 0
        while i < len(s):
            if s[i] == '(':
                str1 = ""
                j = i + 1
                while s[j] != ')':
                    str1 += s[j]
                    j += 1

                if str1 in mp:
                    ans += mp[str1]
                else:
                    ans += "?"

                i = j
            else:
                ans += s[i]
            i += 1
        return ans
