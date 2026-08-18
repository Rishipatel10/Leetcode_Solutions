class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = nums[0]
        maxi = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                ans += nums[i]
            else:
                ans = nums[i]
            maxi = max(maxi,ans)
        return maxi