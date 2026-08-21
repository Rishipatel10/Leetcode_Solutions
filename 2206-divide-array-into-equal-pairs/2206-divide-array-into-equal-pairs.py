class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        arr1 = []
        nums.sort()
        for i in range(0,len(nums),2):
            arr1.append(nums[i])
        arr2 = []
        for i in range(1,len(nums)+1,2):
            arr2.append(nums[i])
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True