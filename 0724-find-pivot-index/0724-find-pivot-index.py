class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        left[0] = nums[0]
        for i in range(1,len(nums)):
            left[i] = left[i-1] + nums[i]
            
        right = [0] * n
        right[n-1] = nums[n-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] + nums[i]

        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1