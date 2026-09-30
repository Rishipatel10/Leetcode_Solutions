class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        ans = []
        for i in range(len(nums)):
            if len(ans) < 2:
                ans.append(nums[i])
            elif nums[i] != ans[-2]:
                ans.append(nums[i])

        for i in range(len(ans)):
            nums[i] = ans[i]
        return len(ans)
