class Solution:
    def checkRecord(self, s: str) -> bool:
        c1 = 0
        c2 = 0
        maxi= 0
        for i in range(len(s)):
            if s[i] == 'A':
                c1 += 1
            if s[i] == 'L':
                c2 += 1
            else:
                c2 = 0
            maxi = max(maxi,c2)
        return (c1 < 2) and (maxi < 3)