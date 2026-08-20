class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxi = max(nums)
        c = 0
        for i in range(len(nums)):
            if nums[i] < maxi:
                num = nums[i]
                while num != maxi:
                    num += 1
                    c += 1
        return c
