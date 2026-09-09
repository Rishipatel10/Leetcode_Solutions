class Solution:
    def countCommas(self, n: int) -> int:
        c = 0
        if n >= 1000:
            c += (n + 1 - 1000)

        if n >= 1000000:
            c += (n + 1 - 1000000) 

        if n >= 1000000000:
            c += (n + 1 - 1000000000)

        if n >= 1000000000000:
            c += (n + 1 - 1000000000000) 
        
        if n >= 1000000000000000:
            c += (n + 1 - 1000000000000000)
        return c