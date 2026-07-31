class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            mini = 0

            for i in range(1,len(nums)):
                if nums[i]<nums[mini]:
                    mini = i

            nums[mini] *= multiplier
        return nums
