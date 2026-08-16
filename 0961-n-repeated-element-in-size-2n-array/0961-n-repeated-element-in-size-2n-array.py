class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        dict1 = defaultdict(int)

        for i in nums:
            dict1[i]+=1
            
        for i in nums:
            if dict1[i] == n:
                return i
