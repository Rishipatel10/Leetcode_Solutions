from collections import *
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dict1 = defaultdict(int)
        for i in range(len(s)):
            dict1[s[i]] += 1
        ans = []
        for n , c in dict1.items():
            ans.append(c)
        for i in range(len(ans)-1):
            if ans[i] != ans[i+1]:
                return False
        return True