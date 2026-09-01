from collections import *
class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = defaultdict(int)
        while n:
            d = n % 10
            freq[d] += 1
            n //= 10
        ans = 0
        for n,c in freq.items():
            ans += n*c

        return ans