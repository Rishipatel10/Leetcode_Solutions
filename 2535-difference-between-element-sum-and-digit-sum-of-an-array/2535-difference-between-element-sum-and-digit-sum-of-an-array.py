class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = 0
        
        sum2 = 0
        for i in range(len(nums)):
            sum1+=nums[i]
            num = nums[i]
            while num>0:
                d = num % 10
                sum2+=d
                num //= 10
        return abs(sum1 - sum2)