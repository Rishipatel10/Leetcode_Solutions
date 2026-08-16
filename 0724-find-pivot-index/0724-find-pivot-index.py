class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        left [0] = nums[0]
        for i in range(1,len(nums)):
            left[i] = nums[i] + left[i-1]
            
        right[n-1] = nums[n-1]
        for i in range(len(nums)-2,-1,-1):
            right[i] = nums[i] + right[i+1]

        for i in range(len(left)):
            if left[i] == right[i]:
                return i
        return -1 
