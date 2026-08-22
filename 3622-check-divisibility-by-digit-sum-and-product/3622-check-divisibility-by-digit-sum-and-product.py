class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum1 = 0
        mul = 1
        temp = n
        while temp:
            d = temp % 10
            sum1 += d
            mul *= d
            temp //= 10
        if n % (sum1 + mul) == 0:
            return True
        return False