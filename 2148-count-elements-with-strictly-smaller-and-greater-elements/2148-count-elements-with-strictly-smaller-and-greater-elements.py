class Solution:
    def countElements(self, nums: List[int]) -> int:
        maxi = max(nums)
        mini = min(nums)
        c = 0
        for i in nums:
            if i < maxi and i > mini:
                c += 1

        return c