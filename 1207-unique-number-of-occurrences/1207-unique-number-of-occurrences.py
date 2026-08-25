from collections import *
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = defaultdict(int)
        for i in arr:
            freq[i] += 1
        ans = []
        for n,c in freq.items():
            ans.append(c)
        if len(ans) != len(set(ans)):
            return False
        return True