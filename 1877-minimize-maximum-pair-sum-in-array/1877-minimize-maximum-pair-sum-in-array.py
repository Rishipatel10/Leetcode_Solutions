class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        maxi = -100
        while l < r:
            ans = nums[l]+nums[r]
            maxi = max(maxi,ans)
            l+=1
            r-=1
        return maxi