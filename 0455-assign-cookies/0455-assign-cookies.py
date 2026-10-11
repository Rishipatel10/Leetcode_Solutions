class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        n = 0
        m = 0
        c = 0
        while n <= len(g)-1 and m <= len(s)-1:
            if g[n] <= s[m]:
                c += 1
                m += 1
                n += 1
            else:
                m += 1
        return c