class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        def backtrack(start, arr, total):
            if total == target:
                ans.append(arr.copy())
                return
            if total > target:
                return
                
            for i in range(start, len(candidates)):
                arr.append(candidates[i])
                backtrack(i, arr, total + candidates[i])
                arr.pop()
        backtrack(0, [], 0)

        return ans