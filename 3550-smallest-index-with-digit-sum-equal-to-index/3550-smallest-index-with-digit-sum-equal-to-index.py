class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            ans = 0
            while n:
                d = n % 10
                ans += d
                n //= 10
            if ans == i:
                return i
        return -1
