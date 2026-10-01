class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for n , c in count.items():
            if c == 1:
                return n

        