class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        n = len(nums)
        nums.sort()
        arr1 = []
        for i in range(0,n,2):
            arr1.append(nums[i])
        arr2 = []
        for i in range(1,n+1,2):
            arr2.append(nums[i])

        for i in range(len(arr1)-1):
            if arr1[i] == arr1[i+1] or arr2[i] == arr2[i+1]:
                return False
        return True