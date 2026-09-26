class Solution:
    def maxCoins(self, piles: list[int]) -> int:
        piles.sort()
        l = 0
        r = len(piles) - 1
        ans = 0
        while l < r:
            r -= 1
            ans += piles[r]
            r -= 1
            l += 1
        return ans