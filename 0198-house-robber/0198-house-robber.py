class Solution:
    def rob(self, nums: List[int]) -> int:
        b = 0 
        a = 0
        for i in nums:
            curr = max(a,b+i)
            b = a
            a = curr
        return a