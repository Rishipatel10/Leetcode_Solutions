class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = {}
        for i in range(len(arr)):
            if arr[i] in count:
                count[arr[i]] += 1
            else:
                count[arr[i]] = 1
        ans = []
        for c in count.values():
            ans.append(c)
        if len(ans) == len(set(ans)):
            return True
        return False