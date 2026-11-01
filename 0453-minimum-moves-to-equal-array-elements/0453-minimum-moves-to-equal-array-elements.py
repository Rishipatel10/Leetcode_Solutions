class Solution:
    def minMoves(self, nums: list[int]) -> int:
        mini = min(nums)
        ans = 0
        for i in range(len(nums)):
            ans += nums[i] - mini
        return ans
      