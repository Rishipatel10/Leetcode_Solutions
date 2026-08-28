class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        arr = list(set(nums))
        arr.sort(reverse = True)
        ans = []
        for i in range(k):
            if len(arr) == i:
                break
            ans.append(arr[i])
        return ans