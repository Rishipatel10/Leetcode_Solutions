class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c = 1
        maxi = 0
        if len(nums) == 1:
            return 1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                c += 1
            else:
                c = 1
            maxi = max(maxi,c)
        return maxi
