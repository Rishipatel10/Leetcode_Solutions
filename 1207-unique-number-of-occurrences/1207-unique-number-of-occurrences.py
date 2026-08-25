from collections import *
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1
        ans = []
        for n,c in freq.items():
            ans.append(c)
        ans.sort()
        for i in range(len(ans)-1):
            if ans[i] == ans[i+1]:
                return False
        return True