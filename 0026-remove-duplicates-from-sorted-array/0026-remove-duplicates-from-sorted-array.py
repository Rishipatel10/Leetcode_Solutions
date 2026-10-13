class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = []
        set1 = set()
        for i in range(len(nums)):
            if nums[i] not in ans:
                ans.append(nums[i])
        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)