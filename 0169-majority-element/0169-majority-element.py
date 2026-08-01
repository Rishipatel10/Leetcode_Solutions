class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans1 = defaultdict(int)

        for num in nums:
            ans1[num]+=1

        m = len(nums) // 2

        for i in nums:
            if ans1[i] > m:
                return i