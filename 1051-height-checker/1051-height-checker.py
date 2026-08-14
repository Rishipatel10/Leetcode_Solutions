class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = sorted(heights)
        c = 0
        for i in range(len(heights)):
            if heights[i] != ans[i]:
                c += 1
        return c