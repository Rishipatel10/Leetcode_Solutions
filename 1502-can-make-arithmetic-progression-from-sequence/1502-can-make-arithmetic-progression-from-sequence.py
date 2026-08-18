class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        ans = []
        arr.sort()
        sum1 = 0
        for i in range(1,len(arr)):
            sum1 = arr[i] - arr[i-1]
            ans.append(sum1)
        for i in range(len(ans)-1):
            if ans[i] != ans[i+1]:
                return False
        return True