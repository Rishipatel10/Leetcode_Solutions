class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set1 = set()
        ans = []
        for i in nums:
            set1.add(i)
        for i in range(1,len(nums)+1):
            if i not in set1:
                ans.append(i)
        return ans