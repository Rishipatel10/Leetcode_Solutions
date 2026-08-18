class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            ans.append(i)
        
        for i in nums:
            num = i
            res = 0
            while num:
                d = num %10
                res = res * 10 + d
                num //= 10
            ans.append(res)

        set1 = set()
        for i in range(len(ans)):
            set1.add(ans[i])

        return len(set1)

        