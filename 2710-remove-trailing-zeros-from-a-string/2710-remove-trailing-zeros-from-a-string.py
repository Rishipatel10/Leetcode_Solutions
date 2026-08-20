class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        for i in range(len(num)-1,-1,-1):
            if num[i] == '0':
                num =  num[:i]
            else:
                break
        return num