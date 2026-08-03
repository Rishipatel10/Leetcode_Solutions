class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            list1 = []
            num = i
            while num:
                d = num % 10
                list1.append(d)
                num //= 10
                
            for i in range(len(list1)-1 , -1,-1):
                ans.append(list1[i])
        return ans