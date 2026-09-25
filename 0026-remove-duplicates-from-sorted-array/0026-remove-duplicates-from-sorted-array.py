class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ans = []
        set1 = set()
        for i in range(0,len(nums)):
            if nums[i] not in set1:
                set1.add(nums[i])
                ans.append(nums[i])
            
        for i in range(len(ans)):
            nums[i] = ans[i]

        return len(ans)
        