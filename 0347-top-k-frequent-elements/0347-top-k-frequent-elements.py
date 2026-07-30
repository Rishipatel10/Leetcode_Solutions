from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        ans = []

        for nums,count in freq.most_common(k):
            ans.append(nums)
        return ans