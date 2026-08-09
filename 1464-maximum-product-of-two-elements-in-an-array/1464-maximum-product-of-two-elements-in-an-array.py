class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi = -100
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                ans = (nums[i]-1) * (nums[j]-1) 
                maxi = max(maxi,ans)
        return maxi