class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            ans += nums[j] - nums[i]
            i += 1
            j -= 1
        return ans