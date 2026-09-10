class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        c = 1
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                c += 1
            else:
                c = 1
            if c > k:
                nums.remove(nums[i+1])
            else:
                i += 1

        return nums
