class Solution:
    def isHappy(self, n: int) -> bool:
        while n>5:
            sum1 = 0
            temp = n
            while temp:
                d = temp % 10
                sum1 += d*d
                temp //= 10
            n = sum1
        return n == 1