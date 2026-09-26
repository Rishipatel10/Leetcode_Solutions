class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        candidates.sort()

        def solve(index, arr, total):
            if total == target:
                ans.append(arr.copy())
                return
            if total > target:
                return
            for i in range(index, len(candidates)):

                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                arr.append(candidates[i])

                solve(i + 1, arr, total + candidates[i])

                arr.pop()

        solve(0, [], 0)

        return ans