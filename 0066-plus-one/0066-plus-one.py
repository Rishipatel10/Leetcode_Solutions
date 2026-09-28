class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in range(len(digits)):
            s += str(digits[i])
        n  = 0
        n = int(s) + 1
        ans = str(n)
        arr = []
        for i in range(len(ans)):
            arr.append(int(ans[i]))
        return arr