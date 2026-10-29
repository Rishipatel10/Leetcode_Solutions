class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        ans = [0] * int(len(gain) + 1)
        idx = 1
        for i in range(len(gain)):
            ans[idx] = ans[idx-1] + gain[i]
            idx += 1
        return max(ans)