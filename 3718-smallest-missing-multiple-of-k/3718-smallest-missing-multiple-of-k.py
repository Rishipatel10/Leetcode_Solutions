class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        ans = 0 
        for i in range(1,120):
            ans = i * k
            if ans not in nums:
                return ans
