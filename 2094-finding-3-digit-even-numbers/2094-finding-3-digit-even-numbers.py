class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        n = len(digits)
        ans = set()
        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if i != k and j != k and digits[k] % 2 == 0:
                        num = digits[i] * 100 + digits[j] * 10 + digits[k]
                        ans.add(num)

        return sorted(ans)
                    