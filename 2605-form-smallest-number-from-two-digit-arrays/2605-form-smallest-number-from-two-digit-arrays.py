class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        c = set(nums1) & set(nums2)
        if c:
            return min(c)
        mini1 = min(nums1)
        mini2 = min(nums2)
        return min(mini1 *10 + mini2,mini2 *10 + mini1)