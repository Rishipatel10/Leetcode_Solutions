class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        t = 0
        ans = 0
        for i in requests:
            t += abs(i - ans)
            ans = i
        return t