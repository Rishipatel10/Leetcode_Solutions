class Solution:
    def canAliceWin(self, n: int) -> bool:
        c = 10
        ans  = 0
        while n >= c:
            n -= c
            ans += 1
            c -= 1
        if ans % 2 == 1:
            return True
        return False