class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        set1 = set()
        duplicate = -1
        for num in nums:
            if num in set1:
                duplicate = num
            set1.add(num)

        mising = -1
        for i in range(1,len(nums)+1):
            if i not in set1:
                missing = i
                break
        
        return [duplicate,missing]